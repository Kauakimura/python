salario = float(input("informe o sue sálario R$"))
if salario > 1250:
    aumento10 = salario + (salario * 0.10)
    print(f"salario atual {salario:.2f} salario com aumento de 10% {aumento10:.2f}")
else:
    aumento15 = salario+(salario *0.15)
    print(f"salario atual {salario:.2f} salario com aumento de 15% {aumento15:.2f}")