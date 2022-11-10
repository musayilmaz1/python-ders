import csv

baslik=["sicaklik","nem","basinc"]
veri=[[30,75.5,10],[32,32.3,50,3]]


with open("sensor_veri.csv",
          "w",encoding="UTF8",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(baslik)
    writer.writerows(veri)
    """for i in veri
    writer.writerow
    döngü ile yapma"""