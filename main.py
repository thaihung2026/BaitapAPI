from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

app = FastAPI()

# 1. Khởi tạo mô hình (Chạy một lần khi bật server)
model_name = "VietAI/vit5-base-vietnews-summarization"
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)

# 2. Định nghĩa cấu trúc dữ liệu đầu vào
class TextRequest(BaseModel):
    text: str

# 3. Chức năng 1: Thông tin giới thiệu (GET /)
@app.get("/")
async def root():
    return {
        "project": "API Tóm tắt văn bản tiếng Việt",
        "model": model_name,
        "description": "Gửi văn bản vào endpoint /predict để nhận bản tóm tắt."
    }

# 4. Chức năng 2: Kiểm tra sức khỏe hệ thống (GET /health)
@app.get("/health")
async def health_check():
    return {"status": "Hoạt động bình thường", "device": device}

# 5. Chức năng 3: Tóm tắt văn bản (POST /predict)
@app.post("/predict")
async def predict(request: TextRequest):
    input_text = request.text.strip()
    
    # Kiểm tra dữ liệu đầu vào (Xử lý lỗi theo yêu cầu đề bài)
    if not input_text:
        raise HTTPException(status_code=400, detail="Văn bản đầu vào không được để trống.")
    if len(input_text.split()) < 20:
        raise HTTPException(status_code=400, detail="Văn bản quá ngắn để tóm tắt (cần ít nhất 20 từ).")

    try:
        # Tiền xử lý văn bản
        text_to_summarize = "vietnews: " + input_text + " </s>"
        encoding = tokenizer(text_to_summarize, return_tensors="pt", max_length=1024, truncation=True)
        input_ids = encoding["input_ids"].to(device)
        attention_mask = encoding["attention_mask"].to(device)

        # Chạy suy luận
        with torch.no_grad():
            outputs = model.generate(
                input_ids=input_ids,
                attention_mask=attention_mask,
                max_length=256,
                early_stopping=True
            )

        # Giải mã kết quả
        summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return {"summary": summary}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi hệ thống trong quá trình xử lý: {str(e)}")