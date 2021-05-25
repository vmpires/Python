num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma = lambda num1, num2 : num1 + num2
subtracao = lambda num1, num2 : num1 - num2
multiplicacao = lambda num1, num2 : num1 * num2
divisao = lambda num1, num2 : num1 / num2

print(f'A soma dos números é: {soma(num1,num2)}')
print(f'A subtração dos números é: {subtracao(num1,num2)}')
print(f'A multiplicação dos números é: {multiplicacao(num1,num2)}')
print(f'A divisão dos números é: {divisao(num1,num2)}')
