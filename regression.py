import numpy as np
from sklearn.linear_model import LinearRegression

# Données
tirant_eau = np.array([1.5, 1.6, 1.8, 2.0]).reshape(-1, 1)  # variable indépendante (X)

# Variables dépendantes (Y)
B1 = np.array([176, 195, 232, 269])
B2 = np.array([184, 203, 241, 279])
B3 = np.array([189, 208, 220, 282])
B4 = np.array([176, 195, 250, 270])
B5 = np.array([201, 220, 258, 300])
B6 = np.array([222, 210, 279, 316])
B7 = np.array([180, 210, 249, 350])

# Fonction pour réaliser une régression linéaire
def regression_lineaire(tirant_eau, B):
    model = LinearRegression()
    model.fit(tirant_eau, B)
    predicted_B = model.predict(tirant_eau)
    return model, predicted_B

# Liste pour stocker les modèles et les prédictions
models = []
predictions = []

# Réaliser la régression pour chaque série B
B_series = [B1, B2, B3, B4, B5, B6, B7]
for B in B_series:
    model, predicted_B = regression_lineaire(tirant_eau, B)
    models.append(model)
    predictions.append(predicted_B)

# Afficher les résultats (pentes et intercepts)
regression_params = [(model.coef_[0], model.intercept_) for model in models]

# Affiche les coefficients de la régression pour chaque série de données
for i, (coef, intercept) in enumerate(regression_params, 1):
    print(f"Série B{i}: pente = {coef:.2f}, intercept = {intercept:.2f}")
