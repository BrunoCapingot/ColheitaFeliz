class Visualizacao():
    def __init__(self):
        self.etapa = 0
        self.listaDeErros = [
            {0:"Operadores negativos não são Validos"},
        ]

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
                3: "Efetuar Pesquisas", 4: "Manejo de Plantaçoes", 5: "Listar Informações",
                6: "Mudar Cenario", 7: "Sair do game"
            }
        ]



    def proximaEtapa(self):
        self.etapa = self.etapa + 1

    def etapaAnterior(self):
        self.etapa -= 1

    def estruturaDaEtapa(self):
        print(self.txtOperacoes[self.etapa])

    def visualizarEtapa(self):
        return self.etapa

    def imprimirOperacao(self):
        print(self.txtOperacoes[self.etapa])

    def ImprimirIndroducao(self):
        print("Colheita Condicional")
        print("Jogue por meio da seleção numerica do teclado que contem como valor o item que você deseja!")

    def Erros(self):
        print(self.listaDeErros[self.etapa])

