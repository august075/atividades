class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 50

    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
        else:
            print("Canal inválido.")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def mostrar_status(self):
        print(f"Canal: {self.canal}")
        print(f"Volume: {self.volume}")


