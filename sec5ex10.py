altura = float(input('Digite sua altura: ').strip())
sexo = input('Digite seu sexo (m ou f): ')
pi = 0
if sexo == 'm':
    pi = (72.7*altura)-58
    print(f'{pi:.2f}')
else:
    pi = (62.1*altura)-44.7
    print(f'{pi:.2f}')

