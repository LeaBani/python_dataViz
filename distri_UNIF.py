import numpy as np
import matplotlib.pyplot as plt

# Paramètres de la loi uniforme
a, b = 15, 30

# Création de valeurs pour l'axe x
x = np.linspace(10, 35, 400)

# Fonction de densité de la loi uniforme
y = np.where((x >= a) & (x <= b), 1 / (b - a), 0)

# Création du graphique
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=f'Loi uniforme U({a}, {b})', color='blue')
plt.fill_between(x, y, where=(x >= a) & (x <= b), color='skyblue', alpha=0.4)

# Ajout d'une ligne verticale pour représenter 18 min
plt.axvline(x=18, color='red', linestyle='--', label="18 min")

# Titres et légendes
plt.title('Représentation de la loi uniforme U(15, 30)')
plt.xlabel('Temps (minutes)')
plt.ylabel('Densité de probabilité')
plt.legend()

# Affichage du graphique
plt.grid(True)
plt.show()
