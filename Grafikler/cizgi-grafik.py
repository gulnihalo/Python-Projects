import matplotlib.pyplot as plt

grafik= plt.figure()
ax1=grafik.add_subplot(311)
ax1.plot([10,40,20])
ax1.plot(range(50))

plt.show()