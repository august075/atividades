class tamaguchi:
    def __init__ (self,nome,fome,saude,idade):
        self.nome=nome
        self.fome=fome
        self.saude=saude
        self.idade=idade

    def alterarnome(self,novonome):
        return self.nome == novonome

    def alterarfome(self,novafome):
        return self.fome==novafome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

tamagushi = Tamagushi ("Meu Tamagushi", 5, 8, 2)
print(tamagushi.retornar_nome())  
print(tamagushi.retornar_fome())  
print(tamagushi.retornar_humor())  

tamagushi.alterar_nome("Novo Tamagushi")
tamagushi.alterar_fome(3)
tamagushi.alterar_saude(6)
tamagushi.alterar_idade(3)

print(tamagushi.retornar_nome())
print(tamagushi.retornar_fome())  
print(tamagushi.retornar_saude())  
print(tamagushi.retornar_idade())  
print(tamagushi.retornar_humor())  

