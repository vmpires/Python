def isPalindrome(frase):
    frase = frase.lower()
    if " " in frase:
        indesejados = ' ,.;:?!-'
        palavra = [c for c in frase if c not in indesejados]
    else:
        palavra = frase
    inicio = 0
    fim = len(palavra)-1
    for i in range(len(palavra)//2):
        if palavra[inicio] != palavra[fim]:
            return False
        inicio += 1
        fim -= 1
    return True


if __name__ == "__main__":
    palavra1 = "Osso"
    palavra2 = "arara"
    palavra3 = "Radar"
    palavra4 = "Tigre"
    palavra5 = "Laranja"

    frase1 = "Ame o Poema!"
    frase2 = "Socorram-me! Subi no onibus em Marrocos!"    

    print(isPalindrome(palavra1))
    print(isPalindrome(palavra2))
    print(isPalindrome(palavra3))
    print(isPalindrome(palavra4))
    print(isPalindrome(palavra5))
    
    print(isPalindrome(frase1))
    print(isPalindrome(frase2))