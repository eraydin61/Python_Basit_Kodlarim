#n! hesaplayan sonksıyon (Böl ve fethet)
def faktoriyel(n):
    print("n=",n," için fonksiyon çarıldı")
    if n==0 or n==1:
        return 1
    else:
        sonuc=n*faktoriyel(n-1)
        print(n,"*",n-1,"! için ara sonuc =",sonuc)
        return sonuc

#n. Fibonacci Sayılarını hesaplayan fonksıyon (Böl Ve Fethet)
def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#n. Fibonacci Sayılarını iteratif(klasık) yöntem ile bulma
def fibonacci2(n):
    if n==0 or n==1:
        return n
    else:
        a=0
        b=1
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return c

#ANA PROGRAM
print(faktoriyel(10))
print(fibonacci(35))
print(fibonacci2(35))
        
