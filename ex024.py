cidade = str(input('Digite a cidade em que você nasceu: ')).strip()
cidade = cidade.split()
cidade[0] = cidade[0].lower()
verif = cidade[0] == 'santo'
print(verif)
