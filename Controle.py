from Model import Modelo


class ControleDeClasses():
    """
    Classe responsável por controlar as operações e etapas do jogo Colheita Condicional.

    Atributos:
    opr (int): valor da operação selecionada pelo usuário.
    validadeDeOperacaes (bool): indica se a operação selecionada pelo usuário é válida ou não.
    etapa (Etapa): objeto da classe Etapa que contém as informações das etapas do jogo.
    Métodos:
    __init__(): inicializa a classe e o jogo.
    operacaoEtapa(): realiza a operação de avançar ou retroceder uma etapa, dependendo da validade da operação selecionada.
    recebeOperacao(): solicita ao usuário que informe uma operação.
    validarOperacao(): verifica se a operação selecionada pelo usuário é válida ou não.
    """

    def __init__(self):
        """
            Inicializa a classe e o jogo, apresentando as instruções iniciais para o usuário.
        """
        self.modelo = Modelo()
        self.opr = 0
        self.validadeDeOperacaes = False


        while self.opr != -69:
            self.modelo.setEtapaAtual()
            self.modelo.visualizarEstruturaEtapa()
            self.recebeOperacao()
            self.validarOperacao()
            self.operacaoEtapa()


    def operacaoEtapa(self):
        """
        Realiza a operação de avançar ou retroceder uma etapa,
         dependendo da validade da operação selecionada.
        """
        if self.modelo.getEtapa() >= 0:
            if self.validadeDeOperacaes == True:
                self.modelo.proximaEtapa()


    def recebeOperacao(self):
        """
            Solicita ao usuário que informe uma operação.
        """
        self.opr = int(input())

    def validarOperacao(self):
        """
           Verifica se a operação selecionada pelo usuário é válida ou não.
        """
        self.validadeDeOperacaes = self.modelo.validarOperacao()



"""
  def validadorDeEtapa(self):
    self.opcao = self.modelo.puxar_opcao()
    print(len(self.opcao))
    if self.numEtapa >= 0 and self.numEtapa >= len(self.opcao):
      print(self.numEtapa)
    if self.validadeDeOperacaes == True:
      self.numEtapa = self.numEtapa + 1
      print(self.numEtapa)
    else:
      self.validadeDeOperacaes == False
      self.numEtapa = self.numEtapa - 1
      print(self.numEtapa)

  def validadorDeOperacacao(self):
    etapa = self.modelo.puxar_etapa()
    opcoes = self.modelo.puxar_opcao()
    if self.opr <= len(opcoes) - 1 and self.opr >= 0:
      print('validado')
      self.validadeDeOperacaes = True
    else:
      self.validadeDeOperacaes = False
      print('Nao validado')
"""

ControleDeClasses()
