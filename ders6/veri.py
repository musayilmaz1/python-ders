import os
import zipfile
import pandas as pd
import sqlite3


from zipfile import ZipFile
if not os.path.exists("veri"):
    os.mkdir("veri")
    arsiv = zipfile.ZipFile("pariteler_cikti_1hour_2022_2022.zip")
    arsiv.extractall(path="veri/")
tum_dosyalar =os.listdir("veri")
print(tum_dosyalar)
print(type(tum_dosyalar))
pandas_csv_listesi=[]
for csv_dosya in tum_dosyalar:
    veri=pd.read_csv("veri/"+csv_dosya)
    del veri["volume"]
    pandas_csv_listesi.append(veri)

birlesmis_csv_ler=pd.concat(pandas_csv_listesi)
birlesmis_csv_ler.to_csv(("hepsi.csv"), index=False)

bag=sqlite3.connect("kripto.vt")
cursor=bag.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS parite("
               +"id INTEGER PRIMARY KEY AUTOINCREMENT,"
               +"otime DATETIME,open FLOAT,"
               +"high FLOAT,low FLOAT,close FLOAT);")
