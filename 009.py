class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Coordenadas do ponto: ({self.x}, {self.y})")


class Retangulo:
    def __init__(self, largura, altura, ponto_inicial):
        self.largura = largura
        self.altura = altura
        self.ponto_inicial = ponto_inicial

    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)


# Criando objetos da classe Retangulo
retangulo1 = Retangulo(5, 3, Ponto(1, 1))
retangulo2 = Retangulo(8, 4, Ponto(2, 2))

# Função para alterar os valores do retângulo e imprimir o centro
def alterar_retangulo(retangulo):
    largura = float(input("Digite a nova largura do retângulo: "))
    altura = float(input("Digite a nova altura do retângulo: "))
    x = float(input("Digite a coordenada x do ponto inicial: "))
    y = float(input("Digite a coordenada y do ponto inicial: "))

    retangulo.largura = largura
    retangulo.altura = altura
    retangulo.ponto_inicial.x = x
    retangulo.ponto_inicial.y = y

    centro = retangulo.encontrar_centro()
    centro.imprimir()


# Menu para alterar os valores do retângulo e imprimir o centro
while True:
    print("1. Alterar retângulo 1")
    print("2. Alterar retângulo 2")
    print("3. Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("Alterando retângulo 1:")
        alterar_retangulo(retangulo1)
    elif opcao == 2:
        print("Alterando retângulo 2:")
        alterar_retangulo(retangulo2)
    elif opcao == 3:
        break
    else:
        print("Opção inválida. Digite novamente.")