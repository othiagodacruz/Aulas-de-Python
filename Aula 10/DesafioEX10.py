import math
import os

#Biblioteca Math

x = 16
raiz_quad = math.sqrt(x)
print("Raiz quadrada de", x, " é igual a", raiz_quad)

angulo = 45
seno = math.sin(angulo)
print("O seno de", angulo, " é igual a", seno)

#Biblioteca OS

diretorio = os.getcwd()
print("O diretorio corrente é", diretorio)

lista = [10, 20, 30]
tam = len(lista)
print("A lista", lista, " tem tamanho", tam)

soma = sum(lista)
print("A lista", lista, " tem um somatório igual a", soma)

# os.system("cls")      -> CLS limpa o Terminal/Tela