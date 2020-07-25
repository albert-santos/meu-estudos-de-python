opção = 'S'
soma = cont = maior = menor = 0
while opção == 'S':
    n = int(input('Digite um número: '))
    opção = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n


média = soma / cont
print('Você digitou {} números e a média foi de {:.2f}'.format(cont, média))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
