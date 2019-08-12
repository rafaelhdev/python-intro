import random
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
lista = 0, 1, 2, 3, 4, 5
a = int(random.choices(lista)[0])
b = int(input('Em que número eu pensei? Digite: '))
print('PROCESSANDO...')
sleep(3)
if a == b:
    print('Você acertou!!!')
else:
    print(f'Eu pensei no {a} e você escreveu {b}.')
    print('Número errado. Tente novamente, parça!')


