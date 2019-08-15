from datetime import date
ano = int(input('Digite o ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
print(anoatual)
print(f'Quem nasceu em {ano} tem {idade} anos de idade.')
if idade == 18:
    print('Você precisa se alistar este ano!')
elif idade > 18:
    print(f'Você passou {idade-18} anos do alistamento.')
elif idade < 17:
    print(f'Faltam {18-idade} anos para seu alistamento.')
