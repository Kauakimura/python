import math
angulo =  float(input("digite o ângulo que vc deseja: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f"o angulo de seno {seno:.2f} \n o angulo de cosseno {cosseno:.2f}\n e o angulo da tangente é {tangente:.2f}")