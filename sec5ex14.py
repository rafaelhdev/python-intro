nota1 = float(input('Digite a primeira nota do aluno (trabalho de laboratório): ').strip())
nota2 = float(input('Digite a segunda nota do aluno (avaliação semestral): ').strip())
nota3 = float(input('Digite a terceira nota do aluno (exame final): ').strip())
media = 0
if (nota1 < 0) or (nota1 > 10) or (nota2 < 0) or (nota2 > 10) or (nota3 < 0) or (nota3 > 10):
    print('Nenhuma das notas pode ser negativa ou maior que 10.')
else:
    media = (nota1*2+nota2*3+nota3*5)/10
if media < 2.9:
    print(media)
    print('Aluno reprovado.')
else:
    if 3.0 < media < 4.0:
        print(media)
        print('Aluno em recuperação.')
    else:
        print(media)
        print('Aluno aprovado!')
