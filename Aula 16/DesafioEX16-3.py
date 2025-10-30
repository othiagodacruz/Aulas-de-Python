print("Seja bem vindo ao contador de 1 a 100!")
print("Vamos revisar os comandos...")
print("Use *Sim* para continuar e *Nao* para parar!")

i = 0

print("Certo, vamos começar a contagem!")
print(i)

for i in range(1,100,1):
    Resposta = input("Você deseja continuar? ")
    if Resposta == "Nao":
        print("Poxa, tudo bem, então vamos finalizar em ", i-1)
        break
    else:
        print("OK, então você deseja continuar! ")
        print(i)