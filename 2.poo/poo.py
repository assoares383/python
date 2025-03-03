# Classe
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    def saudacao(self):
        return(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos')

# Objeto
pessoa1 = Pessoa('João', 20)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa('Maria', 32)
mensagem = pessoa2.saudacao()
print(mensagem)