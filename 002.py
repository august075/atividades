class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, novo_lado):
        self.lado = novo_lado

    def retornarLado(self):
        return self.lado

    def calcularArea(self):
        return self.lado * self.lado

quadrado = Quadrado(5)
print("Lado do quadrado:", quadrado.retornarLado())
print("Área do quadrado:", quadrado.calcularArea())

quadrado.mudarLado(7)
print("Novo lado do quadrado:", quadrado.retornarLado())
print("Nova área do quadrado:", quadrado.calcularArea())