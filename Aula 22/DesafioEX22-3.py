lista_produtos = []

for _ in range(5):
    produto = {}
    produto["nome"] = input("Digite o Nome do Produto: ")
    produto["id"] = int(input("Digite o Número de Identificação: "))
    produto["preco"] = float(input("Digite seu preço: "))
    lista_produtos.append(produto)
    print("Foram Cadastrados ", len(lista_produtos), " Produtos até o momento")

print("Dados do Estoque: ")
for produto in lista_produtos:
    print()
    print("Nome do Produto: ", produto["nome"])
    print("Número de Identificação: ", produto["id"])
    print("Valor do Produto: ", produto["preco"])