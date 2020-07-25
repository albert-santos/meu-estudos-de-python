sexo = str(input('Infrome o seu sexo: [M/F]')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]

print('O sexo registrado foi {}'.format(sexo))
