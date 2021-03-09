import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

#This method uses the 'create' and 'png' methods from 'pyqrcode' to generate the qr code using an specific data
def create_qrcode(data):
    qr_code = pyqrcode.create(data)
    qr_code_img = qr_code.png("qrcode.png", scale=5)
    print("QR Code created succesfully!")

#This method uses the 'decode' method from 'pyzbar' that decodes an instance of 'PIL' (Python Imaging Library) Image and gets its data
def read_qrcode(image):
    data = decode(Image.open(image))
    print(data[0].data.decode())