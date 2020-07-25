num = (int(input('Digite um número: ')), int(input('Digite um número: ')),
       int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')