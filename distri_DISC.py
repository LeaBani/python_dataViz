import numpy as np
import matplotlib.pyplot as plt


# Probabilités cumulées (converties en probabilités non-cumulées)
probabilities = np.array([0.0333, 0.1833, 0.3333, 0.4833])
prob_non_cumulative = np.diff(np.concatenate([[0], probabilities, [1]]))  # Probabilités non cumulées

# Valeurs correspondantes
values = [0, 60, 120, 180, 240]

# Création du graphique
plt.figure(figsize=(8, 5))
plt.bar(values, prob_non_cumulative, width=10, color='lightblue', edgecolor='black')

# Titres et légendes
plt.title('Loi discrète DISC')
plt.xlabel('Valeurs')
plt.ylabel('Probabilités')
plt.xticks(values)

# Affichage du graphique
plt.grid(True)
plt.show()
