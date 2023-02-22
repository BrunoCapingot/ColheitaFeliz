class Etapa():
  def __init__(self):
    self.etapa = 0
    self.txtOperacoes = [{0: "Jogar", 1: "Sair", 2: "Alterar Configurações Padrão"}, {0: "Dinheiro Infinito(Criativo)",1: "Dinheiro Zerado"}]
    self.opcao = self.txtOperacoes[self.etapa]


  def puxar_opcao(self):
    self.self.opcao = self.txtOperacoes[self.etapa]
    return self.opcao
    #setar etapa para pegar opçao.
    #no self.opcoes, as opcoes de operaoes sao definidas pela etapa, ou seja, a cada etapa tera uma opcao assim cada etapa tera uma opção

  def printar_opcao(self):
    print(self.opcao)

  def puxar_opcao(self):
    return self.opcao

  def setar_etapa(self, dt):
    self.etapa = dt

  def puxar_etapa(self):
    etapa = self.etapa
    return etapa
