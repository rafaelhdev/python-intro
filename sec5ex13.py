nota1 = float(input('Digite a primeira nota do aluno: ').strip())
nota2 = float(input('Digite a segunda nota do aluno: ').strip())
nota3 = float(input('Digite a terceira nota do aluno: ').strip())
media = (nota1*1+nota2*1+nota3*2)/4
print(f'A média do aluno foi {media:.2f}.')
if media > 60:
    print('Aluno aprovado.')
else:
    print('Aluno reprovado.')
