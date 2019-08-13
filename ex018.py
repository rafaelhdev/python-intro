import math
n = input('Digite um angulo em graus: ')
angulo = math.radians(float(n))
print(f'O seno de {n} é {math.sin(angulo):.2f}.')
print(f'O cosseno de {n} é {math.cos(angulo):.2f}.')
print(f'A tangente de {n} é {math.tan(angulo):.2f}.')