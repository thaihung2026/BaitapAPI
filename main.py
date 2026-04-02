from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

app = FastAPI()

model_name = "VietAI/vit5-base-vietnews-summarization"
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)

class TextRequest(BaseModel):
    text: str


@app.get("/")
async def root():
    return {
        "project": "API Tóm tắt văn bản tiếng Việt",
        "model": model_name,
        "description": "Gửi văn bản vào endpoint /predict để nhận bản tóm tắt."
    }

@app.get("/health")
async def health_check():
    return {"status": "Hoạt động bình thường", "device": device}

@app.post("/predict")
async def predict(request: TextRequest):
    input_text = request.text.strip()
    
    if not input_text:
        raise HTTPException(status_code=400, detail="Văn bản đầu vào không được để trống.")
    if len(input_text.split()) < 20:
        raise HTTPException(status_code=400, detail="Văn bản quá ngắn để tóm tắt (cần ít nhất 20 từ).")

    try:
        text_to_summarize = "vietnews: " + input_text + " </s>"
        encoding = tokenizer(text_to_summarize, return_tensors="pt", max_length=1024, truncation=True)
        input_ids = encoding["input_ids"].to(device)
        attention_mask = encoding["attention_mask"].to(device)

        with torch.no_grad():
            outputs = model.generate(
            input_ids=encoding["input_ids"].to(device),
            attention_mask=encoding["attention_mask"].to(device),
            max_length=256,      
            min_length=40,      
            num_beams=4,         
            length_penalty=1.0,
            early_stopping=True
            )

        summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return {"summary": summary}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi hệ thống trong quá trình xử lý: {str(e)}")