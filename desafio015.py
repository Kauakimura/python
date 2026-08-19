day = int(input("quantos day alugados? "))
km =  float(input("quantos Km rodados? "))

custo = day * 60
rodado = km * 0.15
print(f"O total  apagar é de {custo + rodado:.2f}")