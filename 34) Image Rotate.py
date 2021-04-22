import os
from PIL import Image
# Write any image path
path = 'Selfportrait.jpg'

colorImage  = Image.open(path)
rotated     = colorImage.rotate(45)
transposed  = colorImage.transpose(Image.ROTATE_180)

transposed.save(path+"_rotate.jpg")
print ('Imagem invertida com sucesso!')
