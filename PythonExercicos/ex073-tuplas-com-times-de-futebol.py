tabela = ('Juventude', 'São José', 'Volta Redonda', 'Ypiranga', 'Remo', 'Paysandu', 'Tombense', 'Boa Esporte', 'Luverdense','Atlético AC')
print(f'Lista de times do grupo B da série C: {tabela}')
print('-='*30)

print(f'Os 5 primeiros do grupo são: {tabela[:5]}')
print('-='*30)

print(f'Os 4 últimos do grupo são: {tabela[-4:]}')
print('-='*30)

print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-='*30)

print(f'O Paysandu está na {tabela.index("Paysandu") + 1}ª posição.')

