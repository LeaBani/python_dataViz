import pandas as pd

# Liste des fichiers et des scénarios correspondants
files_scenarios = {
    'sc1.xlsx': 'Scénario 1',
    'sc2.xlsx': 'Scénario 2',
    'sc3.xlsx': 'Scénario 3',
    'sc4.xlsx': 'Scénario 4',
    'sc5.xlsx': 'Scénario 5',
    'sc6.xlsx': 'Scénario 6',
    'sc1Bis.xlsx': 'Scénario 1 Bis',
    'sc2Bis.xlsx': 'Scénario 2 Bis'
}

# Dictionnaire pour stocker les résultats
results = {}

# Boucle sur chaque fichier et scénario
for file_path, scenario_title in files_scenarios.items():
    # Charger les données depuis le fichier Excel
    data = pd.read_excel(file_path)
    
    # Calculer le nombre total d'observations
    total_count = data['Duration (in Days)'].count()
    
    # Calculer le nombre d'observations supérieures à 5, 6 et 7 jours
    count_above_5 = (data['Duration (in Days)'] > 5).sum()
    count_above_6 = (data['Duration (in Days)'] > 6).sum()
    count_above_7 = (data['Duration (in Days)'] > 7).sum()
    
    # Calculer les pourcentages
    if total_count > 0:  # Éviter la division par zéro
        percentage_above_5 = (count_above_5 / total_count) * 100
        percentage_above_6 = (count_above_6 / total_count) * 100
        percentage_above_7 = (count_above_7 / total_count) * 100
    else:
        percentage_above_5 = percentage_above_6 = percentage_above_7 = 0.0

    # Stocker les résultats
    results[scenario_title] = {
        'Pourcentage > 5 jours': percentage_above_5,
        'Pourcentage > 6 jours': percentage_above_6,
        'Pourcentage > 7 jours': percentage_above_7
    }

# Convertir les résultats en DataFrame
results_df = pd.DataFrame(results).T  # Transposer pour avoir les scénarios en lignes

# Afficher le tableau
print(results_df)

# Optionnel : Enregistrer le tableau dans un fichier Excel
results_df.to_excel('pourcentages_durations.xlsx', index=True)
