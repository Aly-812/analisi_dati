import matplotlib.pyplot as plt

quadrati = [1, 4, 9, 16, 25]
input_valori = [1,2,3,4,5]

plt.style.use('ggplot')

fig, ax = plt.subplots()
ax.plot(input_valori, quadrati, linewidth=3)

ax.set_title("Quadrati dei numeri", fontsize = 24)
ax.set_xlabel("Valore", fontsize = 14)
ax.set_ylabel("Quadrati", fontsize = 14)
ax.tick_params(labelsize = 14)

plt.show()