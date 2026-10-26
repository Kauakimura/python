num1=int(input('informe o primeiro número: '))
num2=int(input('informe o segundo número: '))
num3=int(input('informe o terceiro número: '))

menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
print(f'o menor número é {menor}')
maior = num1
if num2>num1 and num2>num3:
    maior =num2
if num3>num1 and num3>num2:
    maior = num3
print(f'o maior número é {maior}')    

