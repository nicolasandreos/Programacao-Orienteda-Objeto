from datetime import datetime
import pytz
from random import randint

class ContaCorrente():

  @staticmethod
  def data_hora():
    fuso_brasilia = pytz.timezone("America/Sao_Paulo")
    data_hora = datetime.now(fuso_brasilia)
    return data_hora.strftime('%d/%m/%Y %H:%M:%S')

  def __init__(self, nome:str, cpf:str, agencia:int, num_conta:int):
    self._nome = nome
    self._cpf = cpf
    self._saldo = 0
    self._limite = None
    self._agencia = agencia
    self._num_conta = num_conta
    self._transacoes = []
    self.cartoes = []

   

  def depositar(self, valor):
    self._saldo += valor
    self._transacoes.append((f'Valor depositado: R${valor}', f'Saldo Final: R${self._saldo}', ContaCorrente.data_hora()))

  def sacar(self, valor):
    if self._saldo - valor >= self._limite_conta():
      self._saldo -= valor
      self._transacoes.append((f'Valor sacado: R${valor}', f'Saldo Final: R${self._saldo}', ContaCorrente.data_hora()))
    else:
      print('Saldo insuficiente!')

  def transferir(self, valor, conta_destino):
    if self._saldo - valor >= self._limite_conta():
      self._saldo -= valor
      self._transacoes.append((f'Transferencia de R${valor}',f'Para: {conta_destino._nome.capitalize()}', f'Saldo Final: R${self._saldo}', ContaCorrente.data_hora()))
      conta_destino._saldo += valor
      conta_destino._transacoes.append((f'Transferencia de R${valor}',f'Recebida de: {self._nome.capitalize()}', f'Saldo Final: R${conta_destino._saldo}', ContaCorrente.data_hora()))
    else:
      print('Saldo insuficiente!')

  def consultar_saldo(self):
    print(f'Seu saldo atual é de {self._saldo}')

  def consultar_limite(self):
    print(f'O limite da sua conta é de R${self._limite_conta()}')

  def consultar_transacoes(self):
    print('HISTÓRICO DE TRANSAÇÕES')
    for transacao in self._transacoes: print(transacao)

class CartaoCredito():

  @staticmethod
  def data_hora():
    fuso_brasilia = pytz.timezone("America/Sao_Paulo")
    data_hora = datetime.now(fuso_brasilia)
    return data_hora

  def __init__(self, titular, conta_corrente):
    self._num_cartao = randint(1000000000000000, 9999999999999999)
    self._titular = titular
    self._validade = f'{CartaoCredito.data_hora().month}/{CartaoCredito.data_hora().year+4}'
    self._cod_seguranca = str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9))
    self._limite = 1000
    self._senha = '1234'
    self.conta_corrente = conta_corrente
    conta_corrente.cartoes.append(self)

  @property
  def senha(self):
    return self._senha
  
  @senha.setter
  def senha(self, nova_senha):
    if len(nova_senha) >= 4 and nova_senha.isnumeric():
      self._senha = nova_senha
    else:
      print('Senha nao permitida!')
  
