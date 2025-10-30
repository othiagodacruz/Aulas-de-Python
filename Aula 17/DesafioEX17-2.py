minhalista = []
i = 1

print("Seja Bem Vindo!")
print("Vamos montar uma lista?!")
print("Basta você adicionar números inteiros")
print("E quando preferir parar, digite 0")
print("Siga informando conforme eu solicitar!")

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