print('-'*40)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('-'*40)

tot = barato = contmil = 0
while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    if barato == 0:
        barato = preço
        nomeb = nome
    if preço < barato:
        barato = preço
        nomeb = nome
    if preço > 1000:
        contmil += 1
    tot += preço
    while True:
        opção = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if opção in 'SsNn':
            break
    if opção in 'Nn':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R${tot:.2f}')
print(f'Temos {contmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeb} que custa R${barato:.2f}')
