import matplotlib.pyplot as plt
grafik=plt.figure()
ax=grafik.add_axes([0.1,0.1,0.8,0.8])
adet=int(input("Kaç adet ürün girilecek:"))
urun=[]
sayi=[]
for i in range(adet):
    plt.title("Elektronik Ürünler")
    elektronik=input("Elektronik ürün girin:")
    satis=int(input("Satış sayısı girin:"))
    urun.append(elektronik)
    sayi.append(satis)
    
ax.bar(urun,sayi)
plt.show()    
    