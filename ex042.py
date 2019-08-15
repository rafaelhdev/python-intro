lado1 = float(input('Digite a medida do primeiro lado do triângulo: '))
lado2 = float(input('Digite a medida do segundo lado do triângulo: '))
lado3 = float(input('Digite a medida do terceiro lado do triângulo: '))
if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print('ERRO. Algum dos valores digitados foi negativo ou igual a zero.')
elif lado1 > (lado2 + lado3) or lado2 > (lado1 + lado3) or lado3 > (lado1 + lado2):
    print('ERRO. Não é possível formar um triângulo com estes valores.')
elif lado1 == lado2 and lado3 == lado2:
    print('Você formou um triângulo equilátero.')
elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
    print('Você formou um triângulo escaleno.')
elif (lado1 == lado2 and lado2 != lado3) or (lado2 == lado3 and lado3 != lado1) or (lado3 == lado1 and lado1 != lado2):
    print('Você formou um triângulo isósceles.')
