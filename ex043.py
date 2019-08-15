peso = float(input('Digite a massa da pessoa em kg: '))
altura = float(input('Digite a altura da pessoa em metros: '))
imc = peso/(altura*altura)
print(f'O imc dessa pessoa é: {imc}.')
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')