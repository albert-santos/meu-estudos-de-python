casa = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o seu salário: R$'))
anos = int(input('Digite em quantos anos você pretende pagar a casa: '))

meses = 12 * anos
prestacao = casa/meses

if prestacao <= 0.3*sal:
    print('Parabéns, seu empréstimo foi aprovado!')
    print('O valor da pretação mensal será de {.2f}'.format(prestacao))
else:
    print('Seu empréstimo foi negado.')