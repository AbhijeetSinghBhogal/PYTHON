import pyqrcode

# Conda environment "env_pyqrcode"

string = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=104s"

url = pyqrcode.create(string)

# print(url.terminal(quiet_zone = 1))

url.png("/Users/abhijeetsingh/PYTHON/QR_Code_Generator/QR_Code.png", scale = 5)

# url.svg("/Users/abhijeetsingh/PYTHON/QR_Code_Generator/qr_code.svg", scale = 5)