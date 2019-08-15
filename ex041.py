from datetime import date
ano = date.today().year - int(input('Digite o ano de nascimento do atleta: '))
if ano > 0:
    if ano <= 9:
        print('CATEGORIA MIRIM')
    elif 9 < ano <= 14:
        print('CATEGORIA INFANTIL')
    elif 14 < ano <= 19:
        print('CATEGORIA JÚNIOR')
    elif 19 > ano >= 25:
        print('CATEGORIA SÊNIOR')
    elif ano > 25:
        print('CATEGORIA MASTER')
else:
    print('IDADE INVÁLIDA')

