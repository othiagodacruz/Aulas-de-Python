conj1 = {"Carlos", "Josiel", "Jandira", "Aline"}
conj2 = {"Aline", "Carlos", "Jaqueline", "Altair"}

print("O primeiro conjunto é: ", conj1)
print("O segundo conjunto é: ", conj2)

uniao = conj1.union(conj2)
intersec = conj1.intersection(conj2)
difer = conj1.difference(conj2)
diferr = conj2.difference(conj1)

print("Quais pessoas estão presentes no mesmo grupo? \n", intersec)
print("Quais pessoas estão apenas em um grupo? \n", difer, diferr)
print("Lista de todos os envolvidos: \n", uniao)