 #Pesquisa sobre Nível de Satisfação e Tempo de Residência: 
   #A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o nível de satisfação com a cidade e tempo de residência. A prefeitura deseja saber:
   #a) distribuição da população com base no nível de satisfação;
   #b) tempo de residência médio na cidade;
   #c) percentual de pessoas insatisfeitas;
   #d) percentual de pessoas que residem na cidade há mais de 10 anos.
  # Ao final de cada iteração, o usuário deve informar se deseja continuar ou não a responder a pesquisa.

populacao = int(input("me informe a quantidade de população: "))

satisfeitos = 0
insatisfeitos = 0
tempoCidade = 0
for i in range(1, populacao + 1):
    satisfeito = input("vc está satisfeito (s/n): ")

    if satisfeito == 's':
        satisfeitos+=1
    else:
        insatisfeitos+=1

    cont = input("quer continuar (s/n): ")
    if cont == 'n':
        print("fim")
        continue


    tempo = int(input("tempo que vc reside na cidade: "))

    if tempo >= 10:
        tempoCidade+=1

print(f"quantidade de pessoas que estão satisfeitas {satisfeitos} e insatisfeitos {insatisfeitos} ")
print(f"o tempo de residencia media na cidade é {tempo /populacao} ")
print(f"o percentual de possoas insatisfeitas é {(insatisfeitos*populacao)/100}%")
print(f"o percentual de possoas que vivem na cidade a mais de 10 anos é {(tempoCidade * populacao)/100}%")




