from random import randint


class Agencia:

  def __init__(self, telefone, cnpj):
    self.telefone = telefone
    self.cnpj = cnpj
    self.numero = randint(1000, 9999)
    self.clientes = []
    self.caixa = 0
    self.emprestimos = []
    self.minimo_caixa = None

  def consultar_caixa(self):
    print(f'O caixa atual é de R${self.caixa}')

  def verificar_caixa(self):
    print('Caixa abaixo do nivel recomendado') if self.caixa < self.limite_caixa() else print("Caixa acima do nivel recomendado.")

  def limite_caixa(self):
    self.minimo_caixa = 1000000
    return self.minimo_caixa
  
  def adicionar_cliente(self, nome, cpf, patrimonio):
    self.clientes.append((nome, cpf, patrimonio))
    print('Cliente Adicionado com sucesso!')

  def exibir_clientes(self):
    for cliente in self.clientes: print(cliente)

  def emprestimo(self, valor):
    if self.caixa >= valor:
      self.caixa -= valor
      print('Emprestimo Concedido!')
    else:
      print('Caixa Insuficiente!')

  

class AgenciaVirtual(Agencia):
  
  def __init__(self, site, telefone, cnpj):
    super().__init__(telefone, cnpj)
    self.site = site
    self.caixa_paypal = 0

  def depositar_paypal(self, valor):
    self.caixa_paypal += valor
    print('Valor depositado!')

  def sacar_paypal(self, valor):
    if self.caixa_paypal >= valor:
      self.caixa_paypal -= valor
      print('Valor Sacado!')
    else:
      print('Caixa Insuficiente!')


class AgenciaComum(Agencia):
  
  def __init__(self, telefone, cnpj):
    super().__init__(telefone, cnpj)
    self.caixa = 500000


class AgenciaPremium(Agencia):

  def __init__(self, telefone, cnpj):
    super().__init__(telefone, cnpj)
    self.caixa = 10000000
  
  def adicionar_cliente(self, nome, cpf, patrimonio):
    if patrimonio >= 1000000:
      return super().adicionar_cliente(nome, cpf, patrimonio)
    else:
      print('O clientes não possui o patrimonio mínimo necessário pra prosseguir com a criação da conta Premium.')

