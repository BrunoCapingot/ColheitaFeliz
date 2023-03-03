from View import Visualizacao
#Pensamento focado em 3 etapas

class Modelo():
    def __init__(self):
        self.visualizar = Visualizacao()
    def setEtapaAtual(self):
        self.etapa = self.visualizar.visualizarEtapa()
    def visualizarEstruturaEtapa(self):
        self.visualizar.estruturaDaEtapa()

    def etapaAnterior(self):
        self.visualizar.etapaAnterior()

    def proximaEtapa(self):
        self.visualizar.proximaEtapa()

    def getEtapa(self):
        return self.etapa
