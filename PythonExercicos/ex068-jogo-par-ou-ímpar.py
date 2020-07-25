from random import randint
cont = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
while True:
    n = int(input('Diga um valor: '))
    while True:
        jogador = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
        if jogador in 'PpIi':
            break
    computador = randint(1, 10)
    total = n + computador
    print('-' * 20)
    print(f'Você jogou {n} e o computador {computador}. Total de {total} ',end='')
    if total % 2 == 0:
        print('DEU PAR.')
        resultado = 'P'
    else:
        print('DEU ÍMPAR.')
        resultado = 'I'
    if resultado == jogador:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-=' * 20)
        cont += 1
    else:
        print('Você PERDEU')
        print('-=' * 20)
        break
print(f'GAME OVER! Você venceu {cont} veze(s).')
