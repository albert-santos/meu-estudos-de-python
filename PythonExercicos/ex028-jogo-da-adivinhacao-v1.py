from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinha...')
print('-=-' * 20)
computador = randint(0, 5) #Computador "pensa" em um número
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você me venceu!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}'.format(computador, jogador))
