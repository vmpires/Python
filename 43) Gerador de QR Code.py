import pyqrcode
import png
from pyqrcode import QRCode

# Link desejado para QR Code
QRString = 'http://github.com/vmpires'

# Monta a QR Code
url = pyqrcode.create(QRString)

# Salva o QR Code gerado no local desejado
url.png(r'qr.png', scale=12)