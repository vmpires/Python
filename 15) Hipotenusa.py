import math
cat1 = float(input("Informe o valor do primeiro cateto: "))
cat2 = float(input("Informe o valor do segundo cateto: "))
quadhip = (cat1**2) + (cat2**2)
hip = math.sqrt(quadhip)
print(f'A hipotenusa dos catetos informados é {hip}')