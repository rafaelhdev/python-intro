nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))
media = (nota1+nota2)/2
if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:
    if media >= 7:
        print('ALUNO APROVADO.')
        print(f'A média do aluno foi: {media}')
    elif media < 3:
        print('ALUNO REPROVADO.')
        print(f'A média do aluno foi: {media}')
    elif media >=3 and media <7:
        print('ALUNO EM RECUPERAÇÃO.')
        print(f'A média do aluno foi: {media}')
else:
    print('NOTA INVÁLIDA.')