#Pesquisa sobre Sexo e Estado Civil: 
  # A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o sexo e estado civil. A prefeitura deseja saber:
  # a) distribuição da população por sexo;
  # b) percentual de pessoas solteiras;
  # c) quantidade de pessoas casadas;
  # d) percentual de pessoas divorciadas.
   #Ao final de cada iteração, o usuário deve informar se deseja continuar ou não a responder a pesquisa.

populacao = int(input("Informe a quantidade de população: "))

branco = 0
preto = 0
pardo = 0
amarelo = 0
superiorCompleto = 0
medioIncompleto = 0

for i in range(1, populacao +1):
    
    corPele = str(input("informe a cor da pele entre (branco,preto,pardo,amarelo)")).lower()

    if corPele == "branco":
        branco += 1
        print(f"quantidade de pessoas da cor branca é {branco}")
    elif corPele == "preto":
        preto +=1
        print(f"quantidade de pessoas da cor preta é {preto}")
    elif corPele == "pardo":
        pardo +=1
        print(f"quantidade de pessoas da cor parda é {pardo}")
    else:
        print(f"quantidade de pessoas da cor amarela é {amarelo}")
        amarelo += 1

    cont = input("quer continua? (s/n): ")

    if cont == 'n':
        print("fim da entrevista")
        continue

    ensinoSuperior = input("vc tem o ensino superior completo sim=(1) ou não=(0): ")

    if ensinoSuperior == 1:
        superior += 1
        porcentualSuperior = superior * populacao / 100
        
        continue

    cont = input("quer continua? (s/n): ")

    if cont == 'n':
        print("fim da entrevista")
        continue
    
    ensinoMedio = input("vc tem o ensino medio incompleto sim=(1) ou não=(0): ")

    if ensinoMedio == 1:
        medio += 1
        porcentualMedio = medio * populacao /100
        continue

print("="*100)
print(f"o total de pessoas com cor de pele branca é {branco}, da cor preta é {preto}, da cor parda é {pardo}, da cor amarela é {amarelo}")
print(f"pessoas com o ensino superior completo é de {ensinoSuperior} {superior} ")
print(f"pessoas com o ensino médio incompleto é de {medioIncompleto} {medio} ")
