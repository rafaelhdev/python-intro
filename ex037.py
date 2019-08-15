x = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: \n')
print('[ 1 ] Converter para BINÁRIO \n')
print('[ 2 ] Converter para OCTAL \n')
print('[ 3 ] Converter para HEXADECIMAL \n')
base = int(input('Digite sua opção: '))
if base == 1:
    print(f'Em binário: {str(bin(x))[2:]}')
elif base == 2:
    print(f'Em octal: {str(oct(x))[2:]}')
elif base == 3:
    print(f'Em hexadecimal: {str(hex(x))[2:]}')
else:
    print('Opção inválida!')

