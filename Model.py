from View import Visualizacao


class Modelo():
    def __init__(self):
        self.visualizar = Visualizacao()
        self.etapa = []
    def setEtapaAtual(self):
        self.etapa = self.visualizar.visualizarEtapa()
    def visualizarEstruturaEtapa(self):
        self.visualizar.estruturaDaEtapa()

    def proximaEtapa(self):
        self.opcao = self.txtOperacoes[self.etapa]

    def etapaAnterior(self):
        self.etapa -= 1
        self.opcao = self.txtOperacoes[self.etapa]

    def getOpcaoValida(self):
        return self.txtOperacoes[self.etapa]

    def getEtapa(self):
        return self.etapa
