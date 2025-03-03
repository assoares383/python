# Exemp,o de heranca normal

class Animal: 
    def __init__(self, nome) -> None:
        self.nome = nome
    def emitir_som(self):
        pass

class Maminifero(Animal):
    def amamentar(self):
        return f"{self.nome} esta amamentando"
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} esta voando"
    
class Morcego(Maminifero, Ave):
    def emitir_som(self):
        return "Morcegos emitem sons ultrassonicos"
    
morcego = Morcego(nome='Batman')

print("Nome do Morcego: ", morcego.nome)