matriz = []

print("Vamos trabalhar com uma Matriz 3x4!")
print("Para isso, precisamos que você siga os passos a seguir")
print("Preenchendo as linhas conforme o seu agrado.")

for i in range(3): #pois são 3 linhas
    linha = []
    for j in range(4): #pois são 4 colunas
        print("Estamos na linha:", i, "e na posição:", j)
        dado = int(input(f"Digite o valor de sequência: "))
        linha.append(dado)
    matriz.append(linha)

print("\nPerfeito, a Matriz foi preenchida!")
print("Ela ficou da seguinte maneira:")
for linha in matriz:
    print(linha)

print("Vamos analisar melhor os dados...")

maior = max(max(linha) for linha in matriz)
menor = min(min(linha) for linha in matriz)

print("Maior número digitado:", maior )

print("Menor número digitado:", menor )