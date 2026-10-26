distancia = int(input('informe a distancia da viagem: '))
if distancia <=200:
    valor = distancia *0.50
else:
    valor=distancia * 0.45
print(f"o valor da sua viagem é {valor:.2f}")    