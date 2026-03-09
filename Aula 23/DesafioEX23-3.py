def soma(A, B):
    soma = A + B
    print(f"A soma de {A} + {B} é de {soma}")
    return soma

def subtrai(A, B):
    subtrai = A - B
    print(f"A subtração de {A} - {B} é de {subtrai}")
    return subtrai

def divisao(A, B):
    divisao = A / B
    print(f"A divisao de {A} / {B} é de {divisao}")
    return divisao

def mult(A, B):
    mult = A * B
    print(f"A multiplicação de {A} * {B} é de {mult}")
    return mult

func = input("Escolha a operação (soma, sub, div, mult): ")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if func == "soma":
    res = soma(numero1, numero2)
elif func == "sub":
    res = subtrai(numero1, numero2)
elif func == "div":
    res = divisao(numero1, numero2)
elif func == "mult":
    res = mult(numero1, numero2)
else:
    print("Operação inválida")