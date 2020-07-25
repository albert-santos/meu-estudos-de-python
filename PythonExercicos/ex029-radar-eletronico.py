velocidade = int(input('Qual é a sua velocidade atual do carro? '))

if velocidade > 80:
    valor = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(valor))

print('Tenha um bom dia! Dirija com segurança!')
