n1 = int(input('Digite o primeiro número: ').strip())
n2 = int(input('Digite o segundo número: ').strip())
n3 = int(input('Digite o terceiro número: ').strip())
a = n1 == n2
b = n2 == n3
c = n1 + n2 < n3
d = n2 + n3 < n1
e = n1 + n3 < n2
if a and b:
    print('O triângulo é equilátero.')
elif a or b:
    print('O triângulo é isósceles.')
elif c or d or e:
    print('Não é um triângulo.')
else:
    print('É um triângulo escaleno.')



