import matplotlib.pyplot as plt

from passeggiata_aleatora import PasseggiataAleatoria

#creare l'oggetto Passeggiata aleatoria

pa = PasseggiataAleatoria(5000)


pa.fare_passeggiata()


plt.style.use("dark_background")
fig, ax = plt.subplots()
ax.scatter(pa.x, pa.y, s=20, c= pa.x, cmap = plt.cm.plasma)
plt.show()