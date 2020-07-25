from datetime import date
nasc = int(input("Digite o ano de nascimento: "))
atual = date.today().year
idade = atual - nasc

print("O atleta tem {} anos de idade.".format(idade))

if idade <= 9:
    print("Classificação: MIRIM.")
elif idade <= 14:
    print("Classificação: INFANTIL.")
elif idade <= 19:
    print("Classificação: JUNIOR.")
elif idade <= 25:
    print("Classificação: SÊNIOR.")
elif idade > 25:
    print("Classificação: MASTER.")
    