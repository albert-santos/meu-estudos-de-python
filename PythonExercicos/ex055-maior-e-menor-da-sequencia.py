print('{:=^40}'.format(' MAIOR E MENOR PESO '))

maior = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa em Kg: '.format(c)))
    if peso > maior:
        maior = peso
    if c == 1:
        menor = peso
    if peso < menor:
        menor = peso
print('\nO maior peso iserido foi de {}Kg'.format(maior))
print('O menor peso inserido foi de {}Kg'.format(menor))
