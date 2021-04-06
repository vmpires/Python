import json

with open ("json.txt") as jsonfile:
        texto = json.loads(jsonfile.read())

print (texto["nome"])
print (texto["idade"])
        