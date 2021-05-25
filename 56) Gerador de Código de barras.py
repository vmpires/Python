from barcode import EAN13
from barcode.writer import ImageWriter

# Gera cóodigo de barras desejado
with open (r'C:\Users\50s\Desktop\CódigoDeBarras.jpg','wb') as f:
    EAN13('230819912021', writer=ImageWriter()).write(f)