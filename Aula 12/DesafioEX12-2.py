nome = (input("Digite o seu nome: "))
idade = float(input("Digite a sua idade: "))

if idade >= 18.0:                                            # o IF precisa da condição
    print("Seja muito bem vindo ", nome)
    print("A sua idade é de", idade)
    print("Você é maior de idade!")
else:                                                        # o ELSE sempre vai ser o contrário da condição do IF
    print("Desculpe, mas você ainda é menor de idade!")      # menor que 18 anos, nesse caso...