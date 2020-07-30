from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao


class TestAvaliador(TestCase):

    def setUp(self):
        self.gui = Usuario('Gui')
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular')

    def test_retornar_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        albert = Usuario('Albert')
        lance_do_albert = Lance(albert, 100.0)

        self.leilao.propoe(lance_do_albert)
        self.leilao.propoe(self.lance_do_gui)


        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0


        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_retornar_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        albert = Usuario('Albert')
        lance_do_albert = Lance(albert, 100.0)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_albert)


        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0


        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(150.0, self.leilao.maior_lance)
        self.assertEqual(150.0, self.leilao.menor_lance)


    def test_deve_retornar_o_maior_e_menor_lance_quando_o_leilao_tiver_tres_lances(self):
        albert = Usuario('Albert')
        lance_do_albert = Lance(albert, 100.0)

        vini = Usuario('Vini')
        lance_do_vini = Lance(vini, 200)


        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_albert)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0


        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

