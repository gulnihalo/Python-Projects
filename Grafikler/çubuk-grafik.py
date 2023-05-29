#Sütun grafik oluşturma

import matplotlib.pyplot as plt

grafik=plt.figure()
ax=grafik.add_axes([0.1,0.1,0.8,0.8])
diller=["python","java","c#","php","android","ios\nprogramlama"]
kisiSayisi=[35,30,40,10,45,40]
ax.bar(diller,kisiSayisi)

plt.show()

