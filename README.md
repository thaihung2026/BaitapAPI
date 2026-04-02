# API Tóm Tắt Văn Bản Tiếng Việt (Vietnamese Text Summarization API)

## 📌 Giới thiệu dự án
Dự án này cung cấp một RESTful API dùng để tóm tắt các đoạn văn bản/bài báo tiếng Việt. Hệ thống được xây dựng dựa trên framework **FastAPI** và sử dụng mô hình Trí tuệ Nhân tạo VietAIvit5-base-vietnews-summarization (kiến trúc T5) từ thư viện Hugging Face Transformers.

**Thông tin sinh viên thực hiện:**
- **Họ và tên:** Từ Thái Hưng
- **Mã số sinh viên:** 24120186
- **Môn học:** Tư duy tính toán

---

## 🚀 Công nghệ sử dụng
- **Ngôn ngữ:** Python 3.12 
- **Web Framework:** FastAPI, Uvicorn (ASGI server).
- **AI/Machine Learning:** PyTorch (`torch`), Transformers (`transformers==4.38.2`), SentencePiece.


## Hướng dẫn Cài đặt & Khởi chạy (Local)

### 1. Yêu cầu hệ thống
- Đã cài đặt Python 3.12.x.
- Đã cài đặt môi trường ảo (Virtual Environment).

### 2. Cài đặt thư viện
Kích hoạt môi trường ảo (`.venv`) và chạy các lệnh sau trong Terminal:

```bash
# Cài đặt các thư viện cơ bản từ file yêu cầu
pip install -r requirements.txt

# Cài đặt thư viện bổ trợ xử lý định dạng tệp của mô hình
pip install protobuf

# Hạ cấp transformers về bản ổn định để tương thích với kiến trúc T5
pip install transformers==4.38.2
