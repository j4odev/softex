class Conta:
  def __init__(self, nome, numero, saldo=0):
    self._nome = nome
    self.numero = numero
    self.saldo = saldo

  def sacar(self, valor):
    if self.saldo >= valor:
      self.saldo -= valor
      
  def depositar(self, valor):
    self.saldo += valor

  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self,nome):
    self._nome = nome

  @property
  def numero(self):
    return self.numero

  @numero.setter
  def numero(self, numero):
    if (numero is None) or (numero == 0):
      raise ValueError("Passe uma conta válida!")
      self.numero = numero
