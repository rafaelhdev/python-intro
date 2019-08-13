import math
n1 = float(input('Digite a medida do primeiro cateto: '))
n2 = float(input('Digite a medida do segundo cateto: '))
hip = math.hypot(n1, n2)
print(f'A medida da hipotenusa deste triângulo é: {hip:.2f}.')