class retangulo:
   def __init__(self,base,altura):
    self.base=base
    self.altura=altura

    def retornarlados(self):
         self.base
         self.altura

    def mudarlados(self,nova_altura,nova_base):
        self.base = nova_base
        self.altura = nova_altura
    
    def calcular_area():
        return base * altura / 2

    def calcular_perimetro():
        return (base * 2 ) + (altura * 2)


largura = float(input("Informe a largura do local em metros: "))
comprimento = float(input("Informe o comprimento do local em metros: "))

retangulo1 = retangulo (largura, comprimento)

area_local = retangulo1.calcular_area()
perimetro_local = retangulo1.calcular_perimetro()

tamanho_piso = float(input("Informe o tamanho do piso em metros quadrados: "))
tamanho_rodape = float(input("Informe o tamanho do rodapé em metros lineares: "))

quantidade_pisos = area_local / tamanho_piso
quantidade_rodapes = perimetro_local / tamanho_rodape

print("Quantidade de pisos necessários:", quantidade_pisos)
print("Quantidade de rodapés necessários:", quantidade_rodapes)
