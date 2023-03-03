class Etapa():
    def __init__(self):
        self.etapa = 0
        self.txtOperacoes = [{0: "Jogar", 1: "Sair", 2: "Alterar Configurações Padrão"},
                             {0: "Dinheiro Infinito(Criativo)", 1: "Dinheiro Zerado", 2: "Voltar"},{0:"Entrar no game",1:"Manutenção"}]

    def proximaEtapa(self):
        self.etapa += 1
        self.opcao = self.txtOperacoes[self.etapa]

    def etapaAnterior(self):
        self.etapa -= 1
        self.opcao = self.txtOperacoes[self.etapa]

    def get_opcaoValida(self):
        return self.txtOperacoes[self.etapa]

    def get_etapa(self):
        return self.etapa


