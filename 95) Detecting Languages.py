from langdetect import detect

text1 = "Hello, my name is Victor and I'm 30 years old!"

text2 = "Je m'appelle Victor, je suis un programmateur brasiliene"

print(detect(text1))
print(detect(text2))