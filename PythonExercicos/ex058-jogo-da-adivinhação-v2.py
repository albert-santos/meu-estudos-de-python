from random import randint
from time import sleep
computador = randint(0,10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 10. Tente adivinhar...')
print('-=-' * 20)
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Em que número eu pensei? '))
    tentativas += 1
    if computador == jogador:
        acertou = True
    elif jogador < computador:
        print('Mais... Tente novamente.')
    elif jogador > computador:
        print('Menos... Tente novamente.')
print('\nVocê ACERTOU! E precisou de {} tentativas.'.format(tentativas))


