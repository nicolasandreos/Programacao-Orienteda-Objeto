from ContasBanco import CartaoCredito, ContaCorrente
from Agencia import AgenciaComum, AgenciaPremium, AgenciaVirtual 

conta_nicolas = ContaCorrente('Nicolas', '540.379.608-85', 123, 89672)
conta_nicolas.depositar(500)
cartao_nicolas = CartaoCredito('Nicolas', conta_nicolas)

agencia_virtual = AgenciaVirtual('https://meusite.com.br', 119812313, 7612736712)
agencia_comum = AgenciaComum(119812313, 7612736712)
agencia_premium = AgenciaPremium(11890721, 767386178)

agencia_premium.adicionar_cliente("Jairo", 7867784632, 10000000)
agencia_premium.exibir_clientes()

agencia_comum.adicionar_cliente("Mario", 98237489236, 1000)
agencia_comum.exibir_clientes()
