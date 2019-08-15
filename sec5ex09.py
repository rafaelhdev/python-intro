salario = float(input('Digite seu salário: ').strip())
prest = float(input('Digite o valor da prestação: ').strip())
if prest > 0.2*salario:
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')

