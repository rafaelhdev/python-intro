num1 = float(input('Digite um número: ').strip())
num2 = float(input('Digite outro número: ').strip())
if num1 < 0.0 or num2 < 0.0:
    print('Nenhuma das notas pode ser negativa.')
elif num1 > 10 or num2 > 10:
    print('Nenhuma das notas pode ser maior que 10.')
else:
    media = (num1+num2)/2
    print(f'A média das notas é: {media:.2f}')



