# Rastgele harflerden olusan dosya
import random
def dosyaOlustur(a,d):    # a : her harfin kac kere gectigi listesi
                           #d :  dosya adi
    s=""
    toplam=0
    for i in range(len(a)):
        toplam=toplam+a[i]
    i=0
    while i<toplam:
        harf_kod = random.randint(0,len(a)-1)
        if a[harf_kod]>0:
            a[harf_kod]=a[harf_kod]-1
            s = s + chr(65+harf_kod)
            i = i+1
    # sonucun dosyaya yazılması
    f=open(d,"w")
    f.write(s)
    f.close()
    print("işlem tamamlandı, ",d," dosyasi oluşturuldu!")

# Ana program

# a1 listesi, her harf 100 kere geÃ§iyor
a1=[]
for i in range(26):
    a1.append(100)

# a2 listesi, her harf ASCII kodu kere geÃ§iyor
a2=[]
for i in range(65,91):
    a2.append(i)

# a3 listesi, her harf rastgele sayÄ±da (alt-Ã¼st) aralÄ±ÄŸÄ±nda geÃ§iyor
alt = eval(input("Alt sınırı giriniz : "))
ust = eval(input("üst sınırı giriniz : "))
a3=[]
for i in range(26):
    a3.append(random.randint(alt,ust))

dosyaOlustur(a1,"harfler-a.txt")
dosyaOlustur(a2,"harfler-b.txt")
dosyaOlustur(a3,"harfler-c.txt")
