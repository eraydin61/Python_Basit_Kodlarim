# n adet diski a diskinden c diskine b yi ara disk olarak tasıyan fonksıyon
def hanoi(n,a,c,b):
    if n>=1:  #tasınacak dısk varsa
        hanoi(n-1,a,b,c)
        print(n," numaralı dıskı",a," kulesınden",c," kulesıne tası.")
        hanoi(n-1,b,c,a)

hanoi(10,"A","C","B")
