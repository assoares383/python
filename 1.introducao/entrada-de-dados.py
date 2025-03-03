# Exemplo de "if"
idade = 18

idade = int(input("Quantos anos você tem? "))
if idade >= 18:
  print("Você é maior de idade.")
elif idade >= 12:
  print("Você é um adolescente")
else:
  print("Você é menor de idade.")

mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação"
print(mensagem)