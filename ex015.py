km = float(input('Quantos km você rodou? '))
dias = int(input('Quantos dias você rodou com o carro? '))
print(f'O preço a pagar pelos {km} rodados em {dias} dias é R$ {(60*dias)+0.15*km:.2f}')