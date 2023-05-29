# Sınıftaki kız ve erkek öğrencilerin not dağılım grafiği

import matplotlib.pyplot as plt

plt.title("Dağılım Eğrisi")

kızNot=[45,40,50,70,100,85]
erkekNot=[50,40,30,60,100,80]
notAraligi=[0,20,40,60,80,100]

plt.scatter(notAraligi, kızNot,color="b")
plt.scatter(notAraligi, erkekNot,color="r")

plt.xlabel("Öğrenciler")
plt.ylabel("Genel Notlar")
plt.show()