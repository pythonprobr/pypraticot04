from asyncio.test_utils import TestCase

from githubxml.calculadora import Adicao, Operacao, Diferenca, Calculadora


class OperacaoTests(TestCase):
    def test_raise_not_implement(self):
        operacao = Operacao()
        self.assertRaises(NotImplementedError, operacao.calcular, 1, 1)


class SomaTests(TestCase):
    def test_calcular(self):
        operacao = Adicao()
        self.assertIsInstance(operacao, Operacao)
        self.assertEqual(2, operacao.calcular(1, 1))
        self.assertEqual(2.3, operacao.calcular(1.1, 1.2))


class DiferencaTests(TestCase):
    def test_calcular(self):
        operacao = Diferenca()
        self.assertIsInstance(operacao, Operacao)
        self.assertEqual(0, operacao.calcular(1, 1))
        self.assertAlmostEqual(-0.1, operacao.calcular(1.1, 1.2), places=12)


class CalculadoraTests(TestCase):
    def test_adicionar_operacao(self):
        calculadora = Calculadora()
        adicao = Adicao()
        calculadora.adicionar_operacao('+', adicao)
        self.assertIs(adicao, calculadora.operacao('+'))

    def test_efetuar_operacao(self):
        calculadora = Calculadora()
        operacao = OperacaoMock()
        calculadora.adicionar_operacao('-', operacao)
        self.assertIs(3, calculadora.efetuar_operacao('-', 1, 3))
        self.assertEqual(1, operacao.param)
        self.assertEqual(3, operacao.param1)


class OperacaoMock():
    def __init__(self):
        self.param = None
        self.param1 = None

    def calcular(self, param, param1):
        self.param = param
        self.param1 = param1
        return 3
