num = int(input("informe um número: "))
conversor = int(input("digite 1 para converter para binario, ou 2 para octal, ou 3 para hexadecimal: "))

if conversor == 1:
    print(f"seu número convertido em binario é {bin(num)[2:]}")
elif conversor == 2:
    print(f"seu número convertido em octal é {oct(num)[2:]}")
elif conversor == 3:
    print(f"seu número convertido em hexadecimal é {hex(num)[2:]}")
else:
    print("*_*")    