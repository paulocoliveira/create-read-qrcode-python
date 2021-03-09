from qrcode_lib import create_qrcode, read_qrcode

#Call this method in order to generate a qr code to an specific data
create_qrcode("https://www.linkedin.com/in/pcesar/")

#Call this method in order to read the data in a qr code image
read_qrcode("qrcode.png")