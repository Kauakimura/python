nome = str(input("informe seu nome: ")).strip()
n = nome.split() 
print(f"seu primeiro nome {n[0]}")
print(f"sue ultimo nome {n[len(n)-1]}")