dict1 = {"1":"A", "2":"B", "3":"C"}
dict2 = {"4":"D", "5":"E"}
dict3 = {"6":"F"}

dict1.update(dict2,**dict3) # Método para adicionar mais de 1 dicionário
print(dict1)