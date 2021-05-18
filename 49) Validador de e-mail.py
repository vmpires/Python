from validate_email import validate_email

email = input('Digite um e-mail: ')

if validate_email(email) == True:
    print('Este e-mail é válido!')
else:
    print('Este e-mail é inválido!')
