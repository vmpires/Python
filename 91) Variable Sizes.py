import sys

nome = "Victor"
sobrenome = "Milhome Pires"
idade = 30
hobbies = ["Programar", "Nadar", "Ver filmes", "Ouvir música"]

print(f'Nome tem {sys.getsizeof(nome)} bytes.')
print(f'Sobrenome tem {sys.getsizeof(sobrenome)} bytes.')
print(f'Idade tem {sys.getsizeof(idade)} bytes.')
print(f'Hobbies tem {sys.getsizeof(hobbies)} bytes.')