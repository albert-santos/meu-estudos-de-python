algo = input('Digite algo: ')
print('O tipo primitivo do valor é {}'.format(type(algo)))

print('É um número? {}'.format(algo.isnumeric()))
print('É alfabético? {}'.format(algo.isalpha()))
print('É alfanumérico? {}'.format(algo.isalnum()))
print('Está em maiúsculas? {}'.format(algo.isupper()))
print('Está em minúsculas? {}'.format(algo.islower()))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É decimal? {}'.format(algo.isdecimal()))
print('É um dígito? {}'.format(algo.isdigit()))
print('Está capitalizada? {}'.format(algo.istitle()))
