from datetime import date
atual = date.today().year

maiores = 0
menores = 0
for c in range(1, 8):
    nascimento = int(input('Ano de nascimento da {}ª pessoa: '.format(c)))
    idade = atual - nascimento
    if idade >= 18:
        maiores+=1
    else:
        menores+=1

print('\nDo grupo em questão, {} são maiores de idade e {} são menores de idade.'.format(maiores, menores))
