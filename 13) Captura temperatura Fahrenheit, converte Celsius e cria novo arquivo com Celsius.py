f = open("temperaturas.txt", "rt")

lines = f.read().split('\n')
temperaturas = []
celsius = []
for line in lines:
    temperaturas.append(int(line))

for temperatura in temperaturas:
    temperatura = (temperatura-32) * 5/9
    celsius.append(temperatura)

print (celsius)

file = open("celsius.txt", "w")
for val in celsius:
    file.write(str(val)+'\n')
file.close()
