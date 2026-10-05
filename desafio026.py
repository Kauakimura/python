frase  = str(input('me informe uma frase: ')).upper().strip()

print(f"quantas letra A aparece {frase.count('A')}")
print(f"a primeira letra A aparece {frase.find('A')+1} ")
print(f"a ultima letra A aparecer na posição {frase.rfind('A')+1}")