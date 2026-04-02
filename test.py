import requests

# Đảm bảo bạn đang bật server bằng lệnh: uvicorn main:app --reload
API_URL = "http://127.0.0.1:8000/predict"

data = {
    "text": "Liên đoàn Bóng đá châu Âu (UEFA) đã chính thức áp dụng thể thức thi đấu mới cho UEFA"
    " Champions League (Cúp C1) bắt đầu từ mùa giải 2024-2025. Thay vì chia thành các bảng đấu nhỏ 4 đội"
    " như trước đây, 36 đội bóng tham dự sẽ được gộp chung vào một bảng xếp hạng duy nhất, thi đấu theo "
    "thể thức hệ Thụy Sĩ (Swiss model). Mỗi đội sẽ thi đấu 8 trận gồm 4 trận trên sân nhà và 4 trận"
    " trên sân khách với 8 đối thủ khác nhau. Tám đội đứng đầu bảng xếp hạng chung cuộc sẽ giành vé "
    "tiến thẳng vào vòng 16 đội. Trong khi đó, các đội bóng xếp từ vị trí thứ 9 đến 24 sẽ phải bốc thăm "
    "tham dự vòng play-off hai lượt trận để tranh 8 tấm vé vớt còn lại. Thể thức mới này được kỳ vọng "
    "sẽ mang lại nhiều trận đại chiến hấp dẫn hơn ngay từ giai đoạn đầu của giải đấu, hạn chế những "
    "trận đấu thủ tục, đồng thời gia tăng đáng kể doanh thu bản quyền truyền hình."
}

response = requests.post(API_URL, json=data)

if response.status_code == 200:
    print("Kết quả tóm tắt của ViT5:")
    print("=>", response.json()["summary"])
else:
    print("Lỗi:", response.text)