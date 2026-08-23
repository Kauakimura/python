populacao = int(input("informe a quantidade de populacão: "))

mas = 0
fem = 0
solteiras = 0
casadas = 0
divorciadas = 0

for i in range(1, populacao + 1):
    sexo = input("informe o seu sexo (masculino, feminino): ")

    if sexo == 'masculino':
        mas += 1
    else:
        fem +=1
    conti = input("quer continuar (s/n): ")

    if conti == 'n':
        print("fim")
        continue

    estadoCivil = input("me informe su estado civil (soltero, casado, divorciado): ")

    if estadoCivil == 'soltero':
        solteiras += 1
    elif estadoCivil == 'casado':
        casadas += 1
    else:
        divorciadas += 1 

print(f"a quantidade de masculino {mas} e feminino é {fem}: ")
print(f"a quantidade de solteiros é {solteiras} e de casados é {casadas} e divorsiados é {divorciadas}")  
print(f"o percentual de pessoas solteiras é{(solteiras * populacao) /100}% e de casadas é {(casadas * populacao)/100}% e divorciadas é {(divorciadas *populacao)/100}%")