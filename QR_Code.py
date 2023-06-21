import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4,)
qr.add_data("https://www.youtube.com/@sk.salahuddin6170")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("Sk_Salahuddin.png")
