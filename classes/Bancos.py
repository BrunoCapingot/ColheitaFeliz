class Banco():
  def __init__(self, dt):
    self.nome = dt[0]
    self.numeroBanco = dt[1]
    self.dinheiro = dt[2]

  def getNome(self):
    return self.nome

  def getNumeroBanco(self):
    return self.numeroBanco

  def getDinheiro(self):
    return self.dinheiro

  def setDinheiro(self,dt):
    self.dinheiro = dt

  def setNome(self,dt):
    self.nome = dt

  def setNumeroBanco(self,dt):
    self.numeroBanco = dt

class OperarBanco():
  def __init__(self):
    self.contaBruno = Banco(['Bruno Rodrigues Capingote', 694469, 250])

  def efetuarSaque(self):
    return self.contaBruno.getDinheiro()

  def efetuarDeposito(self):
    return self.contaBruno.getDinheiro()

