print("Seja bem vindo a nossa Máquina de Escrever Digital!")
print("O esquema vai ser simples, basta fazer o seguinte:")
print("Você digita a palavra desejada e insere no Programa")
print("Após isso, vai ser impressa na sequência teclada")
print("E para sair/cancelar, é so digitar /exit")

palavra = ""
novapalavra = input(f"Digite uma Palavra: ")

while novapalavra != "/exit":
    palavra = palavra + " " + novapalavra
    print("Ok, o seu texto ficou da seguinte maneira: ")
    print(palavra)
    novapalavra = input("Digite uma Palavra: ")
        
print("Perfeito, vamos finalizar!")