n = int(input('Digite um número inteiro: ').strip())
div3 = n % 3
div5 = n % 5
if div3 == 0 and div5 == 0:
    print('O número é divisível por 5 e por 3 -> Número inválido.')
elif div3 == 0 and div5 > 0:
    print('O número é divisível por 3 apenas -> Número válido.')
else:
    print('O número é divisível por 5 apenas -> Número válido.')


