'''kendısıne gonderılen sayılardan sadece palındrom olanları toplayan dıgerlerınıde bu toplamdan cıkaran gerı gondern program '''
'''def fonksiyon (*sayi):
    toplam=0
    sayiuzunluk=len(sayi)
    for i in range (1,sayiuzunluk):
        if sayi[i]==(sayiuzunluk-i):'''
def polinDram(*dram):
    toplam=fark=0
    for sayi in dram:
        if str(sayi)==str(sayi)[::-1]:
            print(sayi)
            toplam+=sayi
        else:
            toplam-=sayi
        return toplam

polinDram(10,131,565,858)

#CLASS

class sinif:
    pass
nesne = sinif()
print(type(nesne))

class sinif2:
    a=0
    b="asdasf"
    c=[1,5,8,44]
    def yazdir(self):
        d=100
        print(d,self.a)
yeninesne= sinif2()
yeninesne.yazdir()
yeninesne.a=100
print(yeninesne.b)

def palamut():{print("asdasd")}

#class del
#--------------------------------
class ders:
    metin=""
    def __init__(self,a):
        self.metin=a
nesne1=ders("metin")
print(nesne1.metin)


class ders1:
    metin=""
    def __init__(self,a):
        self.metin=a
    def __del__(self):
        print("beni siliyolar..")
nesne2=ders1("metin")
del nesne2

class ders3:
    metin=""
    def __init__(self,a):
        self.metin=a
    def __str__(self):
        return "yazdirilan: "+self.metin
nesne3=ders3("bla bla")
print(nesne3)
#nesne yazdirilinda __str__ den gelen yazdirilir















