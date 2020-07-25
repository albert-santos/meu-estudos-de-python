salario = float(input('Qual é o salário? '))

if salario > 1250:
    nsalario = salario * 1.10
else:
    nsalario = salario * 1.15

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, nsalario))
