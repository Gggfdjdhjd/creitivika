products=[ "pomit poli", "proteret pil", "postirat veshi"]
a=input()
if a=="dobavit":
    products.append(input("Введите новый элемент списка"))
    products.append(input("Введите новый элемент списка"))
    print(products)
elif a=="vichest":
    b=int(input())
    products.pop(b)
    print(products)
    
