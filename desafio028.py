from random import randint
from time import sleep
computador = randint(0, 5)

n = int(input("informe um numero de 0 a 5: "))
print('processando...')
sleep(2)
if n == computador:
    print("vc acertou")
else:
    print(f"vc errou o número era {computador} e vc colocou {n}")    
