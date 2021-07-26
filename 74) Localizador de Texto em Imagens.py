import easyocr

# Defining language
reader = easyocr.Reader(['pt'])

# Loads e reads the image
results = reader.readtext('placa.png', paragraph=False)

# Show results
for result in results:
    print(f"Posição: {result[0]}\n"
            f"Texto: {result[1]}")