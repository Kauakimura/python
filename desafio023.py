#num = int(input("Informe um número: "))
#n = str(num)
#print(f"unidade: {n[3]}")
#print(f"dezena: {n[2]}")
#print(f"centena: {n[1]}")
#print(f"milhar: {n[0]}")

num = int(input("Informe um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"unidade: {u}")
print(f"dezena: {d}")
print(f"centena: {c}")
print(f"milhar: {m}")