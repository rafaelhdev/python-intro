salario = float(input('Digite o salário: '))
if salario <= 1250:
    aumento = 0.15*salario
else:
    aumento = 0.1*salario
salario = salario + aumento
print(salario)
