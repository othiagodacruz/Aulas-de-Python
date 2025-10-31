minhalista = []
i = 1

print("Seja Bem Vindo!")
print("Vamos montar uma lista?")
print("Basta você adicionar alguns números inteiros")
print("E quando preferir parar com a sequência, digite 0")
print("Então siga informando conforme os passos solicitados a seguir!")

while i != 0:
    dado = int(input("Digite um número inteiro: "))
    if dado == 0:
        break
    minhalista.append(dado)

for elem in minhalista:
    print(elem, end=" ")
    
print("\nVocê digitou ", len(minhalista), "números inteiros.")
print(f"O maior número digitado foi: {max(minhalista)}")
print(f"O menor número digitado foi: {min(minhalista)}")