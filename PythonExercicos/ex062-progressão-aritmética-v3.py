print('{:=^40}'.format(' PROGRESSÃO ARITMÉTICA'))
primeiro = int(input('Informe o primeiro termo: '))
razão = int(input('Informe a razão: '))

termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('\nProgressão finalizada com {} termos mostrados.'.format(total))
