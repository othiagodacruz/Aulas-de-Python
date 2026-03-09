pessoa = {
    "nome": "teste",
    "peso": 0.0,
    "idade": 0
}

print("Dados da pessoa:")
print("Nome:", pessoa["nome"])
print("Peso:", pessoa["peso"])
print("Idade:", pessoa["idade"])

print()

pessoa["nome"] = "Texto"
pessoa["peso"] = 99.99
pessoa["idade"] = 0

print("Dados da pessoa:")
print("Nome:", pessoa["nome"])
print("Peso:", pessoa["peso"])
print("Idade:", pessoa["idade"])

print()

pessoa["nome"] = input("Digite o seu nome: ")
pessoa["peso"] = float(input("Digite o seu peso: "))
pessoa["idade"] = int(input("Digite a sua idade: "))

print()

print("Dados da pessoa:")
print("Nome:", pessoa["nome"])
print("Peso:", pessoa["peso"])
print("Idade:", pessoa["idade"])