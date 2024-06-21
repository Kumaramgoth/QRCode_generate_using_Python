import qrcode
import image

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

data = "https://github.com/Kumaramgoth/QRCode_generate_using_Python?tab=readme-ov-file#qrcode_generate_using_python"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png")


