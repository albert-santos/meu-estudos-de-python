from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

gui = Usuario('Gui')
albert = Usuario('Albert')

lance_do_albert = Lance(albert, 100.0)
lance_do_gui = Lance(gui, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_gui)
leilao.lances.append(lance_do_albert)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'Menor lance: {avaliador.menor_lance} e maior lance: {avaliador.maior_lance}')