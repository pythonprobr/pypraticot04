class Operacao():
    def calcular(self, param, param1):
        raise NotImplementedError()


class Adicao(Operacao):
    def calcular(self, param, param1):
        return param + param1


class Diferenca(Operacao):
    def calcular(self, param, param1):
        return param + param1


class Calculadora():
    def __init__(self):
        self._operacoes = {}

    def adicionar_operacao(self, sinal, operacao):
        self._operacoes[sinal] = operacao

    def operacao(self, sinal):
        return self._operacoes[sinal]

    def efetuar_operacao(self, sinal, param, param1):
        operacao = self._operacoes[sinal]
        return operacao.calcular(param, param1)
