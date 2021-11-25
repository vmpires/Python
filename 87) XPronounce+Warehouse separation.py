def itemCount(string):
    lista = string.split("!")
    lista.pop(0)
    lista.pop(-1)
    newstring = "".join(lista)
    return f"{len(newstring)} itens"

def xPronounce(string):
    lista = string.split()
    for index in range(len(lista)):
        if len(lista[index]) == 1 and lista[index] == "x":
            lista[index] = "ecks"
        if lista[index][0] == "x":
            lista[index] = lista[index].replace("x","z")  
    newstring = " ".join(lista)
    for letter in newstring:
        if letter == "x":
            newstring = newstring.replace("x","cks")           
    return newstring

 
print(itemCount("!00!0!000!00!"))
print(itemCount("00!000!000!"))
print(itemCount("00000!00!0!0000"))

print(xPronounce("Inside the box was a xylophone"))
print(xPronounce("The x ray is excellent"))
print(xPronounce("OMG x box unboxing video x D"))
