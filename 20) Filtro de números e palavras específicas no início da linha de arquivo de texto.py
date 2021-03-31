filename = 'source.txt'
with open(filename) as f:
    lines = f.read()
    texto = []
    for i in range(10):
       lines = lines.replace(str(i), "x")
    for line in lines.split("\n"):
        primeira_palavra = line.split()[0]
        if "confidencial:" not in primeira_palavra:
            texto.append(line)

novo = open ("new.txt", "w")
for val in texto:
    novo.write(str(val)+'\n')