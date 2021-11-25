from captcha.image import ImageCaptcha

# Configuração da imagem
image = ImageCaptcha(width=280, height=90)

# Texto escolhido
captcha_text = 'VmPires'

# Gera imagem do captcha
data = image.generate(captcha_text)

#Salva a imagem no caminho escolhido
image.write(captcha_text, 'captcha.jpg')
