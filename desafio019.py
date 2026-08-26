import random
listaNome = []

for i in range(5):
    nome = input("informe um nome: ")
    listaNome.append(nome)

sorteio = random.choice(listaNome)     
print(sorteio)    
