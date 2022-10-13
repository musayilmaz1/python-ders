'''print("5 tane sayi giriniz")
sayi1=input()
sayi2=input()
sayi3=input()
sayi4=input()
sayi5=input()
liste=[sayi1,sayi2,sayi3,sayi4,sayi5]
print(type(liste[0]))'''

liste=[]
'''for i in range(0,5):
    liste.append(eval(input()))'''
def siralama_fonk(a):
    return a*a-20
liste.sort(key=siralama_fonk)
print(liste)
a=5
c=4
d=-5
if a>c:
    print("a c den buyuktur")
if d<0: print("d 0 dan kucuk")
if d>0: print("asd");print("asdasd");d=5

if a>5:
    print("a 5 den buyuktur")
elif a==5:
    print("a 5e esit")
else:
    print("a 5 den kucuk")
b=5
print("a ile b farkli") if a!=b else print("a ile b ayni")
'''---------------------------------'''
a=5
c=10
b=-4

if a<10 or c<10:
    print("a ya da c 10 dan kucuk")

if a ==5 and c==10:
    print("a 5 e esit ve c 10 a esit")
a=4
c=11
if a<5:
    if c >10:
        print("selam")

if a>5:
    pass
print("asdasd")

while a<15:

    a += 1
    if a==8:
        continue
    if a ==12:
        break
    print(a)


else:
    print("a artik 15 yada daha buyuk")
for i in range(0,10):
    print(i)
    for i in range(0,10,2):
        print(i)
liste=["as",True,1.6,5,["asdasd","asd","asdasd"]]

for i in liste:
    print(i)
for i in liste[4]:
    print(i)
for i in range(0,3):
    print(i)
else:
    print("for bitti")
for i ,eleman in enumerate(liste):
    print(i+1,". eleman:",eleman, sep="")

