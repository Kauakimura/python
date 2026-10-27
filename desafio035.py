r1 =float(input("primeiro segmento: "))
r2 =float(input("segundo segmento: "))
r3 =float(input("terceiro segmento: "))
if r1 <r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('o segumento acima é um triângulo')
else:
    print('o segmento acima não é um triângulo')    