from random import shuffle
nome = 0
lista = []
while nome < 10:
    nomes = str(input("informe um nome: "))
    lista.append(nomes)
    nome += 1

shuffle(lista)
grupo1 = lista[:5]
grupo2 = lista[5:] 
print(f"grupo A: {grupo1}")
print(f"grupo B: {grupo2}")