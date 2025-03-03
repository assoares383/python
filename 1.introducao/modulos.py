print("Exemplo de importacao de um modulo padrao:")

from math import sqrt

raiz_quadrada = sqrt(25)
print(f"Raiz quadrada de 25 e {raiz_quadrada}")

print("Exemplo de criacao e utilizacao de um modulo personalizado")
from meu_modulo import saudacao, dobro

mensagem = saudacao("Alexandre")
resultado = dobro(5)

print(mensagem)
print(f"""O dobro de 5 e {resultado}""")