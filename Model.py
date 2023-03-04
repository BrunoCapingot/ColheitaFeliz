from View import Visualizacao
#Pensamento focado em 3 etapas

class Modelo():
    def __init__(self):
        self.visualizar = Visualizacao()
        self.etapa = 0
    def setEtapaAtual(self):
        self.visualizar.visualizarEtapa()

    def visualizarEstruturaEtapa(self):
        self.visualizar.estruturaDaEtapa()

    def etapaAnterior(self):
        self.visualizar.etapaAnterior()

    def proximaEtapa(self):
        self.visualizar.proximaEtapa()

    def getOpcaoValida(self):
        return self.txtOperacoes[self.etapa]

    def getEtapa(self):
        return self.etapa

    def validarOperacao(self):
        """
           Verifica se a operação selecionada pelo usuário é válida ou não.
        """
        if self.visualizar.visualizarEtapa() >= 0 and self.visualizar.visualizarEtapa() < 10:
            return True