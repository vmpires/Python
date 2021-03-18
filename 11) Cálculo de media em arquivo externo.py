f = open("numeros.txt", "rt")
media = 0

lines = f.read().split('\n')
values = []
for line in lines:
    values.append(int(line))

media = sum(values) / len(values)


print (media)