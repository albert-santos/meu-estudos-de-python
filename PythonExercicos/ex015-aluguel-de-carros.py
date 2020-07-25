dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

pdia = 60 * dias
pkm = km * 0.15
tot = pdia + pkm
print('O total a pagar é R${:.2f}'.format(tot))
