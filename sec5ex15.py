dia = int(input('Digite um inteiro entre 1 e 7: '))
if 1 <= dia <= 7:
    if dia == 1:
        print('Segunda-Feira')
    elif dia == 2:
        print('Terça-feira')
    elif dia == 3:
        print('Quarta-feira')
    elif dia == 4:
        print('Quinta-feira')
    elif dia == 5:
        print('Sexta-feira')
    elif dia == 6:
        print('Sábado')
    elif dia == 7:
        print('Domingo')
else:
    print('Número inválido.')

