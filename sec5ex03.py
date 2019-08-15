num = float(input('Digite um número: ').strip())
if num > 0:
    raiz = pow(num,0.5)
    print(f'A raiz de {num:.2f} é {raiz:.2f}.')
else:
    elev = pow(num,2)
    print(f'O número {num:.2f} elevado ao quadrado é {elev:.2f}.')
