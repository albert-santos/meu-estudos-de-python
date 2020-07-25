print('{:=^40}'.format(' LOJAS ALBERT '))
preço = float(input("Preço das compras: R$"))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opção = int(input("Qual é a opção? "))

if opção == 1:
    valor = preço * 0.9
elif opção == 2:
    valor = preço * 0.95
elif opção == 3:
    valor = preço
    preçoparcela = valor / 2
    print("Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.".format(preçoparcela))
elif opção == 4:
    valor = preço * 1.20
    parcelas = int(input("Quantas parcelas? "))
    preçoparcela = valor / parcelas
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS.".format(parcelas, preçoparcela))
else:
    print("Opção invalida! Tente novamente.")

print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preço, valor))
