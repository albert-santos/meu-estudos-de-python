sal = float(input('Qual o salário do funcionário? R$'))

nsal = sal * 1.15
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(sal, nsal))
