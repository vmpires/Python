import matplotlib.pyplot as plt

fig, ax = plt.subplots()
circle = plt.Circle((0,0), 0.55, color="white")
lbls = ['Comer', 'Estudar', 'Codar', 'Dormir', 'Nadar', 'Jogando']

ax.pie([1, 2, 2, 7, 1, 1.5],
        labels=lbls,
        autopct="%1.1f%%",
        pctdistance=.82)
ax.add_artist(circle)
ax.set_title("Victor's Donut Chart", fontsize = 16)
plt.show()
