from time import sleep
print('{:=^40}'.format(' CRIANDO UM MENU '))

opção = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('>>>> Digite a sua opção: '))

    if opção == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif opção == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif opção == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}.'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {} o maior é {}.'.format(n1, n2, n2))
        else:
            print('Os números são iguais.')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando... ')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
sleep(2)
print('Fim do programa! Volte sempre!')
