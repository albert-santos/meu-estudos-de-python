print('{:=^40}'.format(' ANALISADOR COMPLETO '))

media = 0
idademaior = 0
menosde20 = 0
maisvelho = ''
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()


    media = media + (idade/4)
    if idade > idademaior and sexo == 'M':
        idademaior = idade
        maisvelho = nome

    if sexo == 'F' and idade < 20:
        menosde20 += 1

print('{:=^30}'.format(' Análise do Grupo '))
print('Média de idade do grupo: {:.1f}'.format(media))
print('Homem mais velho: {}.'.format(maisvelho))
print('Quantidade de mulheres com idade abaixo de 20 anos: {}.'.format(menosde20))