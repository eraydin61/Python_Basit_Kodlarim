# Gönderilen a parametresi düzgün bir matris ise True;
# değilse False yanıtını geri döndüren fonksiyon
def matrisMi(a):
    if type(a) is list:   #a'nın tipi liste ise
        if (type(a[0])) is list:
            j=len(a[0])
            i=1    # satır numarası
            matris=True   # ilk kabulümüz
            while i<len(a) and matris==True:
                if (type(a[i]) is list) and len(a[i])==j:
                    i=i+1
                else:
                    matris=False
            # while döngüsünden cıktıklarında
            # matris değişkeninin son durumu
            # döndürülmesi gereken degerdir.
            return matris                      
        else:
            return False
    else:
        return False
# a ve b parametreleri aynı satır ve sutun sayısına sahip
# matrisler ise True; aksi taktirde False döndür.
def boyutAyniMi(a,b):
    if matrisMi(a)==True and matrisMi(b)==True:
        if (len(a)==len(b)) and (len(a[0])==len(b[0])):
            return True
        else:
            return False
    else:
        return False
def matrisTopla(a,b):
    if (boyutAyniMi(a,b)==True):
        c=[]
        for i in range(len(a)):   # len(b) de yazilabilirdi.
            satir=[]
            for j in range(len(a[0])):  # sutun sayısı
                satir.append(a[i][j]+b[i][j])
            c.append(satir)
        return c    # sonuc matrısı dondurur
    else:
        print("Parametrelerde Hata Var ! Toplanamaz!")

        
#ANA PROGRAM
x=[[1,4,6],[2,2,5],[3,3,9],[0,5,3],[0,5,2]]
y=[[8,6,4],[1,0,3],[3,2,7],[1,1,2],[4,8,3]]
z=[]

z=matrisTopla(x,y)
print(z)

