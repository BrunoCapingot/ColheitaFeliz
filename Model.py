from classes import Ambiente


class Modelo():
    def __init__(self):
        self.ambiente = Ambiente.Ambiente()
        self.etapa = 0
        self.txtOperacoes = [
            {
                0: "Jogar", 1: "Sair", 2: "Alterar Configurações Padrão"
            },
            {
                0: "Dinheiro Infinito(Criativo)", 1: "Dinheiro Zerado", 2: "Voltar"
            },
            {
                0: "Entrar no game", 1: "Manutenção"
            },
            {
                0: "Desbloquar Areas", 1: "Construir", 2: "Atualizar Construções",
                3: "Efetuar Pesquisas", 4: "Manejo de Plantaçoes", 5: "Listar Informações", 6: "Mudar Cenario",
                7: "Sair do game"
            }
        ]

    def defineAmbiente(self):
        self.ambiente.definicaoDeAmbiente()

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
