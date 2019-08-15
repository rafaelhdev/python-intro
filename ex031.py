viagem = int(input('Digite a distância da viagem, em km: '))
if viagem < 200:
    preco = 0.5*viagem
else:
    preco = 0.45*viagem
print(f'O preço da viagem é: R${preco:.2f}')
