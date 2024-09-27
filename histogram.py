import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier Excel
file_path = 'test.xlsx'  # Remplace par le chemin correct 
data = pd.read_excel(file_path)

print(data.head())

# Créer un histogramme des durées
plt.figure(figsize=(10, 6))
plt.hist(data['Duration (in Days)'].dropna(), bins=20, color='blue', edgecolor='black')

# Ajouter un titre et des labels
plt.title('Fréquence des durées Scénario 2', fontsize=15)
plt.xlabel('Durée (en jours)', fontsize=12)
plt.ylabel('Fréquence', fontsize=12)

# Afficher l'histogramme
plt.show()
