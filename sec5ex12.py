from math import log10
num = int(input('Digite um número inteiro e maior que zero: ').strip())
if num < 0:
    print('Número inválido.')
else:
    a = log10(num)
print(a)