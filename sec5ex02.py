num = float(input('Digite um número: ').strip())
if num > 0:
    raiz = pow(num,0.5)
    print(f'A raiz de {num:.2f} é {raiz:.2f}.')
else:
    print('Número inválido.')
