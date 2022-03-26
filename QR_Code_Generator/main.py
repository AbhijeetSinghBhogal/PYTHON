import pyqrcode

string = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=104s"

url = pyqrcode.create(string)

# print(url.terminal(quiet_zone = 1))

url.png("/Users/abhijeetsingh/PYTHON/QR_Code/qr_code.png", scale = 5)

# url.svg("/Users/abhijeetsingh/PYTHON/QR_Code/qr_code.svg", scale = 5)