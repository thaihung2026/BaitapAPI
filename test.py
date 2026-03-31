import requests

# Thay bằng đường link Pinggy của bạn nếu chạy trên Colab
API_URL = "http://127.0.0.1:8000/predict" 

data = {
    "text": "Đại học Quốc gia Thành phố Hồ Chí Minh (ĐHQG-HCM) là một trong hai hệ thống đại học quốc gia của Việt Nam,"
    " được đánh giá là một trong 1000 trường/hệ thống trường đại học tốt nhất thế giới. Trụ sở chính của ĐHQG-HCM tọa lạc tại"
    " khu đô thị Đại học Quốc gia Thành phố Hồ Chí Minh, thuộc thành phố Dĩ An, tỉnh Bình Dương."
}

response = requests.post(API_URL, json=data)

if response.status_code == 200:
    print("Kết quả tóm tắt:")
    print(response.json()["summary"])
else:
    print("Lỗi:", response.text)