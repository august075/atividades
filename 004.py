class pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


    pessoa1 = pessoa("João", 18, 70, 170)
    print(f"Nome: {pessoa1.nome}")
    print(f"Idade: {pessoa1.idade}")
    print(f"Peso: {pessoa1.peso}")
    print(f"Altura: {pessoa1.altura}")

    pessoa1.envelhecer()
    print(f"Idade após envelhecer: {pessoa1.idade}")
    print(f"Altura após envelhecer: {pessoa1.altura}")

    