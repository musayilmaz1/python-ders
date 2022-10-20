dosya=open("metin.txt","r")
print(dosya.readline())
print(dosya.read(2))
for satir in dosya:
    print(satir[:-1])