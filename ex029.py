velocidade = float(input('\033[33mDigite a velocidade do carro:\033[m '))
if velocidade > 80:
    multa = (velocidade-80)*7
    print(f'Você foi MULTADO!! \n A multa vai custar R${multa:.2f}!')
else:
    print('Velocidade adequada. Dirija com cuidado.')
