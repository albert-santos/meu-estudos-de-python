print('{:=^40}'.format(' PROGRESSÃO ARITMÉTICA '))
primeiro = int(input('Informe o primeiro termo: '))
razão = int(input('Informe a razão da PA: '))

termo = primeiro
cont = 1

while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razão
    cont += 1
print('Fim')
