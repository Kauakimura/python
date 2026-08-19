prod  = float(input("qual o valor do produto? R$ "))

des = prod - (prod * 5 /100)
print(f"o produto que custa R${prod:.2f}, na promoção com desconto de 5% vai custar R${des:.2f}")