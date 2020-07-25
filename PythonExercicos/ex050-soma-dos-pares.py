print('{:=^40}'.format(' SOMA DE PARES '))

s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1

print('\nA soma dos {} números pares informados é igual a {}.'.format(cont, s))