valor_casa =float(input("calor da casa R$"))
salario = float(input("salário do comprador R$"))
anos_financiamento = int(input("quantos anos de financiamento: "))

prestacoes = valor_casa /(anos_financiamento * 12)
minimo = salario+(salario * 0.30)
print(f"para pagar uma casa de R${valor_casa:.2f} em {anos_financiamento} o emprestimo será de R${prestacoes:.2f}")
if prestacoes <= minimo:
    print("emprestimo pode ser concedido")
else:
    print("emprestimo negado")