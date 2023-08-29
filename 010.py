class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor_abastecido):
        litros_abastecidos = valor_abastecido / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return litros_abastecidos
        else:
            return "Não há combustível suficiente na bomba."

    def abastecer_por_litro(self, litros_abastecidos):
        valor_a_pagar = litros_abastecidos * self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return valor_a_pagar
        else:
            return "Não há combustível suficiente na bomba."

    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade_combustivel):
        self.quantidade_combustivel = nova_quantidade_combustivel


# Exemplo de uso da classe BombaCombustivel
bomba = BombaCombustivel("Gasolina", 4.5, 1000)

litros_abastecidos = bomba.abastecer_por_valor(50)
print(f"Foram abastecidos {litros_abastecidos} litros.")

valor_a_pagar = bomba.abastecer_por_litro(20)
print(f"O valor a pagar é R${valor_a_pagar}.")

bomba.alterar_valor(5.0)
bomba.alterar_combustivel("Etanol")
bomba.alterar_quantidade_combustivel(800)


