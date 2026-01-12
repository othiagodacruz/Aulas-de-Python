conj1 = {1, 2, 3, 4} #conjunto base
conj2 = {3, 4, 5, 6}

print("O primeiro conjunto é: ", conj1)
print("O segundo conjunto é: ", conj2)

uniao = conj1.union(conj2)
intersec = conj1.intersection(conj2)
difer = conj1.difference(conj2)

print("O resultado da União entre eles é: ", uniao)
print("O resultado da Intersecção é de: ", intersec)
print("O resultado da Diferença entre eles é de: ", difer)