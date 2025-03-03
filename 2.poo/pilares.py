# Exemplo de heranca
print('\nExemplo de heranca')
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    def andar(self):
        print(f'{self.nome} está andando')
        return
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return 'Au Au'
    
class Gato(Animal):
    def emitir_som(self):
        return 'Miau'
    
# Polimorfismo

dog = Cachorro(nome='Rex')
cat = Gato(nome='Felix')

print("\nExemplo de polimofirsmo")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz {animal.emitir_som()}")

# Encapsulamneto
print('\nExemplo de Encapsulamento')
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo # atributo privado
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    def sacar(self, valor):
        if valor > 0 and  valor <= self.__saldo:
            self.__saldo -= valor
    def get_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancaria: {conta.get_saldo()}")
conta.depositar(valor=300)
print(f"Saldo da conta bancaria: {conta.get_saldo()}")
conta.depositar(valor=-400)
print(f"Saldo da conta bancaria: {conta.get_saldo()}")
conta.sacar(valor=700)
print(f"Saldo da conta bancaria: {conta.get_saldo()}")

conta_do_zezinho = ContaBancaria(saldo=50)
print(f"Saldo da conta do Zezinho: {conta_do_zezinho.get_saldo()}")

print('\nExemplo de abstracao')
from abc import ABC, abstractmethod 

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass
    def ligar(self):
        print('Carro ligado usando a chave')
    def desligar(self):
        print('Carro desligado usando a chave')

carro_anarelo = Carro()

carro_anarelo.ligar()
carro_anarelo.desligar()