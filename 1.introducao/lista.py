# Declaracao

minha_lista = [1, 2, 3, 4, 5, "python", True, False]

# Exibindo a lista
print(minha_lista)

# Exibindo um item
print(minha_lista[1])

# Exibindo um item dentro de um intervalo
print(minha_lista[1:6])

# Exibindo um elemento ate o numero inserido no segundo indice dentro do array
print(minha_lista[:5])

# Pulando os dois primeiros valores do array
print(minha_lista[2:])

# O metodo append adiciona um item no final da lista
minha_lista.append(100)
print(minha_lista)

# O metodo index retorna o valor do primeiro elemento encontrado
indice = minha_lista.index(4)
print(indice)

# O metodo insert insere um elemento em um indice especifico
minha_lista.insert(8, 10000)
print(minha_lista)

# Metodo pop
elemento_removido = minha_lista.pop(7)
print(elemento_removido)
print(minha_lista)

# Metodo Remove
minha_lista.remove(4)
print('Apos remove (4)', minha_lista)

