print('\033[1;31;43mOlá mundo \033[m')
print('\033[4;30;45mOlá Mundo\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m !!! '.format(a, b))

cores = {'limpa':'\033[m'}
nome = 'Albert'
print('Olá! Muito prazer em te conhecer, {}{}{} !!'.format('\033[4;34m', nome, cores['limpa']))
