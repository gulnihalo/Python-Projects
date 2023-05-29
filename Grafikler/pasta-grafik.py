import matplotlib.pyplot as plt

plt.title("Pasta Dilim Grafiği\nProgram Dilleri")

diller=["python","java","c#","php","android","ios\nprogramlama"]
kisiSayisi=[35,30,40,10,45,40]

plt.pie(kisiSayisi,labels=diller, autopct="%1.0f%%")  #%1.2 ise %15.00 %1.0 ise %15 yani 0lar gider

plt.show()
