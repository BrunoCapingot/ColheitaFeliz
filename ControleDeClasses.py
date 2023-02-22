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
    self.numEtapa = 0
    self.opcao = None
    while self.opr != -69:
      self.etapa = Etapa()
      self.etapa.printar_opcao()
      self.etapa.setar_etapa(self.numEtapa)

      self.recebeOperacao()
      self.validadorDeOperacacao()
      self.validadorDeEtapa()

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
  def recebeOperacao(self):
    self.opr = int(input())
  def validadorDeOperacacao(self):
    etapa = self.etapa.puxar_etapa()
    opcoes = self.etapa.puxar_opcao()
    if self.opr <= len(opcoes) - 1 and self.opr >= 0:
      print('validado')
      self.validadeDeOperacaes = True
    else:
      self.validadeDeOperacaes = False
      print('Nao validado')


if __name__ == "ControleDeClasses":
  ControleDeClasses()
