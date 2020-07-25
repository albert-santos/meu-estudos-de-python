print('{:=^40}'.format(' SOMA DE ÍMPARES MÚLTIPLOS DE TRÊS '))

s=0
qtd = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        qtd += 1
print('A soma total dos {} números solicitados é igual a {}.'.format(qtd, s))
