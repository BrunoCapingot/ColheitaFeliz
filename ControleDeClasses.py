from Banco import OperarBanco
from classeEtapa import Etapa


class ControleDeClasses():
  """


  """

  def __init__(self):
    print("Colheita Condicional")
    print("Jogue por meio da seleção numerica do teclado que contem como valor o item que você deseja!")
    self.opr = 0
    self.validadeDeOperacaes = False
    self.etapa = Etapa()
    while self.opr != -69:

      self.etapa.printar_opcao()
      self.recebeOperacao()
      self.validarOperacao()
      self.operacaoEtapa()


  def operacaoEtapa(self):
    if self.etapa.puxar_etapa() >= 0:
      if self.validadeDeOperacaes == True:
        self.etapa.proximaEtapa()
      else:
        self.etapa.etapaAnterior()

  def recebeOperacao(self):
    self.opr = int(input())

  def validarOperacao(self):

    if self.opr >= 0 and self.opr <= len(self.etapa.puxar_opcao())-1:
      print("Operador dentro do intervalo")
      self.validadeDeOperacaes = True
    else:
      print("Operador fora do intervalo")
      self.validadeDeOperacaes = False





"""
  def validadorDeEtapa(self):
    self.opcao = self.etapa.puxar_opcao()
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
    etapa = self.etapa.puxar_etapa()
    opcoes = self.etapa.puxar_opcao()
    if self.opr <= len(opcoes) - 1 and self.opr >= 0:
      print('validado')
      self.validadeDeOperacaes = True
    else:
      self.validadeDeOperacaes = False
      print('Nao validado')
"""

if __name__ == "ControleDeClasses":
  ControleDeClasses()
