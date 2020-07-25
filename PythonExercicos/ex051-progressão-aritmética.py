print('{:=^40}'.format(' Progressão Aritmética '))

ptermo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
décimo = ptermo + (10 - 1) * razão

for c in range(ptermo, décimo + razão, razão):
    print('{}'.format(c), end = '→ ')
print('FIM')

