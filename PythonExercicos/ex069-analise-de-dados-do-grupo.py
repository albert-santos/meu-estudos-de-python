homens = maisdezoito = mulhermenor = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: ')).strip().upper()[0]
        if sexo in 'MmFf':
            break
    if idade > 18:
        maisdezoito += 1
    if idade < 20 and sexo == 'F':
        mulhermenor += 1
    if sexo in 'mM':
        homens += 1
    while True:
        opção = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if opção in 'sSnN':
            break
    if opção == 'N':
        break
print('{:=^40}'.format(' FIM DO PROGRAMA '))
print(f'Total de pessoas com mais de 18 anos: {maisdezoito}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulhermenor} mulheres com menos de 20 anos.')