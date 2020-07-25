for c in range(0, 6):
    print('Oi', end='')
print('\nFim')

for c in range(1, 7):
    print(c, end='')
print('\nFim')

for c in range(6, 0, -1):
    print(c,end='')
print('\nFim')

for c in range(0, 11, 2):
    print(c,end='')
print('\nFim')

i = int(input('Início: '))
f = int(input('Fim: '))
p= int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c, end='')
print('\nFim')

s=0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}.'.format(s))

