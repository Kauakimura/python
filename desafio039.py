from datetime import date
ano= int(input("ano que vc nasceu: "))
hj=date.today().year
idade=hj - ano
print(f"você nasceu em {ano} tem {idade} anos em {hj}")
if idade == 18 :
    print("vc tem que se alistar imediatamente")
elif idade >18:
    saldo = idade -18
    print(f"vc deveria ter se alistado ha {saldo} ano")
    ano_alistamento = hj -saldo
    print(f"seu alistamento foi em {ano_alistamento}")
else:
    saldo = 18 - idade
    print(f"ainda falta {saldo} anos para o alistamento")
    ano_alistamento = saldo + hj
    print(f"seu alistamento será em {ano_alistamento}")    