# 💼 Sistema Bancário POO com Python

Este projeto é um sistema bancário simples, construído com **Programação Orientada a Objetos (POO)** em Python. Ele simula agências, contas correntes e cartões de crédito com funcionalidades reais, como transferências, saques, depósitos e gerenciamento de clientes.

## 🚀 Como executar

1. Clone o repositório:
2. 
   ```bash
   git clone https://github.com/nicolasandreos/Programacao-Orienteda-Objeto
   cd Programacao-Orienteda-Objeto
   ````

3. Execute o projeto:

   ```bash
   python main.py
   ```

---

## 🧠 Conceitos Aplicados

* Herança
* Encapsulamento
* Métodos estáticos e propriedades
* Polimorfismo (sobrescrita de métodos)
* Organização modular
* Simulação de operações bancárias

---

## 📝 Arquivo `main.py`

Este é o ponto de entrada do projeto, onde:

* Uma conta é criada para o usuário.
* Um cartão de crédito é vinculado à conta.
* Três tipos de agência são instanciadas.
* Clientes são adicionados e exibidos.

### 🔁 Exemplo de uso:

```python
conta_nicolas = ContaCorrente('Nicolas', '540.379.608-85', 123, 89672)
conta_nicolas.depositar(500)
cartao_nicolas = CartaoCredito('Nicolas', conta_nicolas)

agencia_premium.adicionar_cliente("Jairo", 7867784632, 10000000)
agencia_comum.adicionar_cliente("Mario", 98237489236, 1000)
```

---

## 🏦 Módulo `Agencia.py`

Este módulo define uma classe base `Agencia` e três subclasses:

### ✅ `class Agencia`

Atributos principais:

* `telefone`, `cnpj`, `numero` (aleatório), `clientes`, `caixa`, `emprestimos`
* Métodos: `consultar_caixa`, `verificar_caixa`, `limite_caixa`, `adicionar_cliente`, `emprestimo`

---

### 🌐 `class AgenciaVirtual(Agencia)`

Extensão de `Agencia`, adiciona:

* `site`: endereço do site
* `caixa_paypal`: valor disponível no PayPal
* Métodos extras: `depositar_paypal`, `sacar_paypal`

---

### 🏢 `class AgenciaComum(Agencia)`

* Caixa inicial: R\$500.000

---

### 💎 `class AgenciaPremium(Agencia)`

* Caixa inicial: R\$10.000.000
* Restrições: só permite clientes com patrimônio ≥ R\$1.000.000

---

## 💰 Módulo `ContasBanco.py`

Define classes para manipulação de contas bancárias e cartões.

### 🧾 `class ContaCorrente`

Atributos:

* `_nome`, `_cpf`, `_saldo`, `_agencia`, `_num_conta`, `_transacoes`, `cartoes`

Métodos:

* `depositar`, `sacar`, `transferir`
* `consultar_saldo`, `consultar_limite`, `consultar_transacoes`

---

### 💳 `class CartaoCredito`

Atributos:

* `_num_cartao`, `_titular`, `_validade`, `_cod_seguranca`, `_limite`, `_senha`, `conta_corrente`

Recursos:

* Validação de senha (mínimo 4 dígitos numéricos)
* Criação automática de número de cartão e código de segurança
* Vinculação direta à conta corrente

---

## 📌 Exemplo prático completo:

```python
from ContasBanco import CartaoCredito, ContaCorrente
from Agencia import AgenciaComum, AgenciaPremium, AgenciaVirtual 

conta_nicolas = ContaCorrente('Nicolas', '540.379.608-85', 123, 89672)
conta_nicolas.depositar(500)
cartao_nicolas = CartaoCredito('Nicolas', conta_nicolas)

agencia_virtual = AgenciaVirtual('https://meusite.com.br', 119812313, 7612736712)
agencia_comum = AgenciaComum(119812313, 7612736712)
agencia_premium = AgenciaPremium(11890721, 767386178)

agencia_premium.adicionar_cliente("Jairo", 7867784632, 10000000)
agencia_comum.adicionar_cliente("Mario", 98237489236, 1000)
```

---

## 📚 Requisitos

* Python 3.8 ou superior
* Biblioteca externa:

  * `pytz`: para timezone no histórico de transações

Instalação do `pytz`:

```bash
pip install pytz
```

---

## 📄 Licença

Este projeto está sob a licença MIT.

