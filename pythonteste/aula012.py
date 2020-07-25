nome = str(input('Qual o seu nome? '))
if nome == 'Albert':
    print('Bem vindo de volta')
elif nome == 'Paulo' or nome == 'Pedro' or nome == 'Maria':
    print('Legal, seu nome é bíblico')
elif nome in 'Ana Jéssica Alice':
    print('Belo nome feminino')
else:
    print('Olá')
print('Tenha um bom dia {}!'.format(nome))
