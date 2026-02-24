# 💼 OOP Banking System with Python

This project is a simple banking system built using **Object-Oriented Programming (OOP)** in Python.  
It simulates bank branches, checking accounts, and credit cards with real-world operations such as transfers, withdrawals, deposits, and client management.

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/nicolasandreos/Programacao-Orienteda-Objeto
cd Programacao-Orienteda-Objeto
```

2. Run the project:

```bash
python main.py
```

---

## 🧠 Applied Concepts

- Inheritance  
- Encapsulation  
- Static methods and properties  
- Polymorphism (method overriding)  
- Modular organization  
- Banking operations simulation  

---

## 📁 Project Structure

```bash
Programacao-Orienteda-Objeto/
│
├── main.py
├── Agencia.py
└── ContasBanco.py
```

---

## 📝 `main.py`

This is the entry point of the project, where:

- A checking account is created
- A credit card is linked to the account
- Three types of bank branches are instantiated
- Clients are added and displayed

### 🔁 Example Usage:

```python
conta_nicolas = ContaCorrente('Nicolas', '540.379.608-85', 123, 89672)
conta_nicolas.depositar(500)
cartao_nicolas = CartaoCredito('Nicolas', conta_nicolas)

agencia_premium.adicionar_cliente("Jairo", 7867784632, 10000000)
agencia_comum.adicionar_cliente("Mario", 98237489236, 1000)
```

---

## 🏦 `Agencia.py` Module

This module defines a base class `Agencia` and three subclasses.

### ✅ `class Agencia`

Main attributes:

- `telefone`, `cnpj`, `numero` (random), `clientes`, `caixa`, `emprestimos`

Main methods:

- `consultar_caixa`
- `verificar_caixa`
- `limite_caixa`
- `adicionar_cliente`
- `emprestimo`

---

### 🌐 `class AgenciaVirtual(Agencia)`

Extends `Agencia` and adds:

- `site`: website address  
- `caixa_paypal`: available PayPal balance  

Additional methods:

- `depositar_paypal`
- `sacar_paypal`

---

### 🏢 `class AgenciaComum(Agencia)`

- Initial balance: R$500,000

---

### 💎 `class AgenciaPremium(Agencia)`

- Initial balance: R$10,000,000  
- Restriction: only allows clients with assets ≥ R$1,000,000  

---

## 💰 `ContasBanco.py` Module

Defines classes for handling bank accounts and credit cards.

---

### 🧾 `class ContaCorrente`

Attributes:

- `_nome`
- `_cpf`
- `_saldo`
- `_agencia`
- `_num_conta`
- `_transacoes`
- `cartoes`

Methods:

- `depositar`
- `sacar`
- `transferir`
- `consultar_saldo`
- `consultar_limite`
- `consultar_transacoes`

---

### 💳 `class CartaoCredito`

Attributes:

- `_num_cartao`
- `_titular`
- `_validade`
- `_cod_seguranca`
- `_limite`
- `_senha`
- `conta_corrente`

Features:

- Password validation (minimum 4 numeric digits)
- Automatic generation of card number and security code
- Direct linking to a checking account

---

## 📌 Complete Practical Example

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

## 📚 Requirements

- Python 3.8 or higher  

External library:

- `pytz` (used for timezone handling in transaction history)

Install dependency:

```bash
pip install pytz
```

---

## 🎯 Learning Objectives

This project was developed to practice:

- Object-Oriented Programming in Python  
- Class relationships and inheritance  
- Encapsulation and data protection  
- Banking logic simulation  
- Modular code organization  

---

## 📄 License

This project is licensed under the MIT License.
```
