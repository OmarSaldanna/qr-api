import os
import qrcode
import hashlib

def crear_qr(contenido):
	# obtener el hexadecimal del contenido
    hash_hex = hashlib.md5(contenido.encode()).hexdigest()
    # establecer la ruta para guardarlo
    ruta = f'{os.environ["SAVE_QRS_ON"]}{hash_hex}.png'
    # crear el qr
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(contenido)
    qr.make(fit=True)
    # establecerlo como imagem
    img = qr.make_image(fill='black', back_color='white')
    # y guardarlo en su ruta
    img.save(ruta)
    return ruta