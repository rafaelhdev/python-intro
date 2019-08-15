x = float(input('Digite o valor da casa: '))
y = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite em quantos anos você quer pagar: '))
prestacao = x / (anos*12)
print(f'Para pagar uma casa de R$ {x} em {anos} anos, a prestação mensal será de R$ {prestacao}.')
print(f'Seu salário é de R$ {y}.')
print(f'30% do seu salário equivale a R$ {0.3*y}.')
if prestacao > 0.3*y:
    print('O valor da prestação ultrapassou 30% do seu salário')
else:
    print('Com o seu salário, você pode comprar essa casa!')
