import pyqrcode
data = input("Enter the link: ")
url = pyqrcode.create(data)
url.svg('qr.svg', scale = 0.5, quiet_zone=8)
url.show()