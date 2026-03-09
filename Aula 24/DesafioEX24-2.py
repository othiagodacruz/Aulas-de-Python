lista_mutavel = [10, 20, 30]

print("Lista Mutável (Antes da Alteração):")
print("Conteúdo:", lista_mutavel)
print("ID:", id(lista_mutavel))

lista_mutavel.append(40)
lista_mutavel[0] = 0

print("Lista Mutável (Depois da Alteração):")
print("Conteúdo:", lista_mutavel)
print("ID:", id(lista_mutavel))