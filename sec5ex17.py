basemaior = float(input('Digite o valor da base maior: ').strip())
basemenor = float(input('Digite o valor da base menor: ').strip())
if basemaior > 0 and basemenor > 0:
    area = (basemaior + basemenor)/2
    print(f'A área do trapézio é: {area:.2f}')
else:
    print('Nenhum dos valores pode ser negativos.')
