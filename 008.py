class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        if len(self.bucho) == 0:
            print(f"{self.nome} está com o bucho vazio.")
        else:
            print(f"{self.nome} tem no bucho: {', '.join(self.bucho)}")

    def digerir(self):
        self.bucho = []

# Testando a classe Macaco
macaco1 = Macaco("Bob")
macaco2 = Macaco("Alice")

macaco1.comer("banana")
macaco1.comer("maçã")
macaco1.comer("laranja")

macaco2.comer("uva")
macaco2.comer("abacaxi")
macaco2.comer("morango")

macaco1.verBucho()
macaco2.verBucho()

macaco1.digerir()
macaco2.digerir()

macaco1.verBucho()
macaco2.verBucho()