# API Tóm Tắt Văn Bản Tiếng Việt (Vietnamese Text Summarization API)

## 📌 Giới thiệu dự án
Dự án này cung cấp một RESTful API dùng để tóm tắt các đoạn văn bản/bài báo tiếng Việt. Hệ thống được xây dựng dựa trên framework **FastAPI** và sử dụng mô hình Trí tuệ Nhân tạo `VietAI/vit5-base-vietnews-summarization` (kiến trúc T5) từ thư viện Hugging Face Transformers.

**Thông tin sinh viên thực hiện:**
- **Họ và tên:** [Điền tên của bạn vào đây]
- **Mã số sinh viên:** [Điền MSSV vào đây]
- **Môn học:** [Điền tên môn học, ví dụ: Thực hành Trí tuệ Nhân tạo / Xây dựng API]

---

## 🚀 Công nghệ sử dụng
- **Ngôn ngữ:** Python 3.12 (Khuyến nghị sử dụng bản ổn định để tránh lỗi tương thích thư viện).
- **Web Framework:** FastAPI, Uvicorn (ASGI server).
- **AI/Machine Learning:** PyTorch (`torch`), Transformers (`transformers==4.38.2`), SentencePiece.
- **Phần cứng:** Hỗ trợ chạy tăng tốc phần cứng trên GPU NVIDIA (CUDA) nếu có (Ví dụ: RTX 2050).

---

## ⚙️ Hướng dẫn Cài đặt & Khởi chạy (Local)

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
