# mess.txt dosya analizi

def algoritma1(mesaj):
    for i in range(len(mesaj)):
        n=mesaj.count(mesaj[i])
        if n==1:
            print(mesaj[i],end=" ")
    
def algoritma2(mesaj):
    h=[]
    for i in range(len(mesaj)):
        if mesaj[i] not in h:
            h.append(mesaj[i])
            n=mesaj.count(mesaj[i])
            if n==1:
                print(mesaj[i],end="")

def algoritma3(mesaj):
    s={}   # Bos sözlük
    for i in range(len(mesaj)):
        if mesaj[i] not in s.keys():
            s[mesaj[i]]=mesaj.count(mesaj[i])
    for a,d in s.items():
        if d==1:
            print(a,end="")

# ANA PROGRAM
#dosyayi oku
f=open("mess.txt","r")
mesaj=f.read()
f.close()

print("Algoritma-1")
algoritma1(mesaj)

print("Algoritma-2")
algoritma2(mesaj)

print("Algoritma-3")
algoritma3(mesaj)













