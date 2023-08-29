class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")


conta = ContaCorrente("123456", "João")
print(f"Número da conta: {conta.numero_conta}")
print(f"Nome do correntista: {conta.nome_correntista}")
print(f"Saldo: {conta.saldo}")

conta.alterarNome("Maria")
print(f"Novo nome do correntista: {conta.nome_correntista}")

conta.deposito(100)
print(f"Saldo após depósito: {conta.saldo}")

conta.saque(50)
print(f"Saldo após saque: {conta.saldo}")