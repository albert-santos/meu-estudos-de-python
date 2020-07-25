print('{:=^40}'.format('TABUADA'))
n = int(input('Digite um número para ver a sua tabuada: '))

print('-' * 13)
for c in range (1, 11, 1):
    print('{} x {:2} = {}'.format(n, c, n * c))
print('-' * 13)