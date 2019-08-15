print("""Digite o número da operação que deseja realizar, conforme a seguir: 
[1] = Soma \n[2] = Subtração \n[3] = Multiplicação \n[4] = Divisão.""")
nop = int(input('-> '))
if 1 <= nop <= 4:
    a = float(input('Digite um número: '))
    b = float(input('Digite outro número: '))
    if nop == 1:
        print(f'O valor da soma entre {a:.2f} e {b:.2f} é {a+b:.2f}.')
    elif nop == 2:
        print(f'O valor da subtração entre {a:.2f} e {b:.2f} é {a - b:.2f}.')
    elif nop == 3:
        print(f'O valor da multiplicação entre {a:.2f} e {b:.2f} é {a * b:.2f}.')
    elif nop == 4:
        print(f'O valor da divisão entre {a:.2f} e {b:.2f} é {a / b:.2f}.')
else:
    print('Número inválido.')
