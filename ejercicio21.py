"""
Ejercicio 21: Machine Learning Basico - Predicciones con Scikit-Learn

Este archivo contiene:
- Regresion Lineal: predecir precios de casas
- Clasificacion Logistica: clasificacion binaria
- Random Forest: multiples arboles de decision
- K-Means: agrupamiento no supervisado
- Evaluacion con metricas (MSE, R2, Accuracy, etc.)
- Visualizaciones con matplotlib

Dataset: dataset_casas.csv (30 casas con caracteristicas)

Como ejecutar:
    python ejercicio21.py

Requisitos:
    pip install scikit-learn pandas numpy matplotlib

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.cluster import KMeans
from sklearn.metrics import (
    mean_squared_error, r2_score, accuracy_score, 
    classification_report, confusion_matrix
)
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("EJERCICIO 21: MACHINE LEARNING BASICO CON SCIKIT-LEARN")
print("=" * 70)

# -----------------------
# 1. CARGAR Y EXPLORAR DATOS
# -----------------------

print("\n[1] CARGANDO Y EXPLORANDO DATOS")
print("-" * 70)

df = pd.read_csv('dataset_casas.csv')
print(f"\nDataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas")
print("\nPrimeras filas:")
print(df.head())
print("\nEstadisticas:")
print(df.describe())

# -----------------------
# 2. PREPARACIÓN DE DATOS
# -----------------------

print("\n\n[2] PREPARACION DE DATOS")
print("-" * 70)

X = df[['tamaño', 'habitaciones', 'baños', 'edad']]
y = df['precio']

print(f"Caracteristicas (X): {X.shape}")
print(f"Variable objetivo (y): {y.shape}")

# Dividir datos: 80% entrenamiento, 20% prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nEntrenamiento: {X_train.shape[0]} muestras")
print(f"Prueba: {X_test.shape[0]} muestras")

# Normalizar datos (importante para mejor rendimiento)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------
# 3. REGRESIÓN LINEAL
# -----------------------

print("\n\n[3] REGRESION LINEAL - Predecir precios")
print("-" * 70)

modelo_lr = LinearRegression()
modelo_lr.fit(X_train, y_train)

# Predicciones
y_pred_lr = modelo_lr.predict(X_test)

# Metricas
mse = mean_squared_error(y_test, y_pred_lr)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_lr)

print(f"\nMetricas:")
print(f"  MSE (Error Cuadratico Medio): ${mse:,.2f}")
print(f"  RMSE (Raiz del MSE): ${rmse:,.2f}")
print(f"  R2 (Coef. de Determinacion): {r2:.4f}")

print(f"\nCoeficientes del modelo:")
for feat, coef in zip(X.columns, modelo_lr.coef_):
    print(f"  {feat}: ${coef:,.2f}")
print(f"  Intercepto: ${modelo_lr.intercept_:,.2f}")

print(f"\nPrimeras 5 predicciones vs reales:")
for i in range(min(5, len(y_test))):
    print(f"  Real: ${y_test.iloc[i]:,.0f} | Predicho: ${y_pred_lr[i]:,.0f}")

# -----------------------
# 4. CLASIFICACIÓN BINARIA (Logística)
# -----------------------

print("\n\n[4] CLASIFICACION LOGISTICA - Casa cara/barata")
print("-" * 70)

# Crear variable binaria: 1 si precio > mediana, 0 si no
precio_mediana = y.median()
y_clasificacion = (y > precio_mediana).astype(int)

# Usar misma division de train/test que la regresion
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
    X, y_clasificacion, test_size=0.2, random_state=42
)

modelo_lg = LogisticRegression(max_iter=1000)
modelo_lg.fit(X_train_clf, y_train_clf)

y_pred_lg = modelo_lg.predict(X_test_clf)
accuracy = accuracy_score(y_test_clf, y_pred_lg)

print(f"\nAccuracy (Precision): {accuracy:.4f} ({accuracy*100:.2f}%)")
print(f"\nReporte de Clasificacion:")
print(classification_report(y_test_clf, y_pred_lg, 
      target_names=['Casa barata', 'Casa cara']))

# -----------------------
# 5. RANDOM FOREST
# -----------------------

print("\n\n[5] RANDOM FOREST - Regresion mejorada")
print("-" * 70)

modelo_rf = RandomForestRegressor(n_estimators=100, random_state=42)
modelo_rf.fit(X_train, y_train)

y_pred_rf = modelo_rf.predict(X_test)
r2_rf = r2_score(y_test, y_pred_rf)
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))

print(f"\nMetricas Random Forest:")
print(f"  R2: {r2_rf:.4f}")
print(f"  RMSE: ${rmse_rf:,.2f}")

print(f"\nImportancia de caracteristicas:")
for feat, imp in zip(X.columns, modelo_rf.feature_importances_):
    print(f"  {feat}: {imp:.4f} ({imp*100:.2f}%)")

# -----------------------
# 6. K-MEANS (Agrupamiento)
# -----------------------

print("\n\n[6] K-MEANS - Agrupamiento de casas")
print("-" * 70)

kmeans = KMeans(n_clusters=3, random_state=42)
grupos = kmeans.fit_predict(X_train_scaled)

print(f"\nCasas agrupadas en {kmeans.n_clusters} clusters")
print(f"\nTamaño de cada cluster:")
for cluster_id in range(kmeans.n_clusters):
    count = (grupos == cluster_id).sum()
    print(f"  Cluster {cluster_id}: {count} casas")

# -----------------------
# 7. VALIDACIÓN CRUZADA
# -----------------------

print("\n\n[7] VALIDACION CRUZADA")
print("-" * 70)

scores = cross_val_score(
    LinearRegression(), 
    X, y, 
    cv=5, 
    scoring='r2'
)

print(f"\nR2 en 5-Fold Cross-Validation:")
print(f"  Scores: {[f'{s:.4f}' for s in scores]}")
print(f"  Media: {scores.mean():.4f} (+/- {scores.std():.4f})")

# -----------------------
# 8. VISUALIZACIONES
# -----------------------

print("\n\n[8] GENERANDO VISUALIZACIONES")
print("-" * 70)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Machine Learning: Regresion y Clasificacion', fontsize=16)

# Regresion Lineal
ax = axes[0, 0]
ax.scatter(y_test, y_pred_lr, alpha=0.6, label='Predicciones')
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 
        'r--', lw=2, label='Perfecto')
ax.set_xlabel('Precio Real ($)')
ax.set_ylabel('Precio Predicho ($)')
ax.set_title(f'Regresion Lineal (R2 = {r2:.4f})')
ax.legend()
ax.grid(True, alpha=0.3)

# Random Forest
ax = axes[0, 1]
ax.scatter(y_test, y_pred_rf, alpha=0.6, color='orange', label='Predicciones')
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 
        'r--', lw=2, label='Perfecto')
ax.set_xlabel('Precio Real ($)')
ax.set_ylabel('Precio Predicho ($)')
ax.set_title(f'Random Forest (R2 = {r2_rf:.4f})')
ax.legend()
ax.grid(True, alpha=0.3)

# Importancia de caracteristicas
ax = axes[1, 0]
importances = modelo_rf.feature_importances_
ax.barh(X.columns, importances, color='green', alpha=0.7)
ax.set_xlabel('Importancia')
ax.set_title('Importancia de Caracteristicas (Random Forest)')
ax.grid(True, alpha=0.3, axis='x')

# Residuos Regresion Lineal
ax = axes[1, 1]
residuos = y_test - y_pred_lr
ax.scatter(y_pred_lr, residuos, alpha=0.6, color='purple')
ax.axhline(y=0, color='r', linestyle='--', lw=2)
ax.set_xlabel('Valores Predichos ($)')
ax.set_ylabel('Residuos ($)')
ax.set_title('Residuos Regresion Lineal')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ml_visualizaciones.png', dpi=100, bbox_inches='tight')
print("\nGraficos guardados en: ml_visualizaciones.png")
plt.show()

# -----------------------
# 9. PREDICCIÓN EN NUEVOS DATOS
# -----------------------

print("\n\n[9] PREDICCION EN NUEVOS DATOS")
print("-" * 70)

nueva_casa = pd.DataFrame({
    'tamaño': [150],
    'habitaciones': [3],
    'baños': [2],
    'edad': [5]
})

prediccion_lr = modelo_lr.predict(nueva_casa)[0]
prediccion_rf = modelo_rf.predict(nueva_casa)[0]

print(f"\nCaracteristicas de la nueva casa:")
print(f"  Tamaño: {nueva_casa['tamaño'].values[0]} m2")
print(f"  Habitaciones: {nueva_casa['habitaciones'].values[0]}")
print(f"  Baños: {nueva_casa['baños'].values[0]}")
print(f"  Edad: {nueva_casa['edad'].values[0]} años")

print(f"\nPredicciones del precio:")
print(f"  Regresion Lineal: ${prediccion_lr:,.0f}")
print(f"  Random Forest: ${prediccion_rf:,.0f}")
print(f"  Promedio: ${(prediccion_lr + prediccion_rf)/2:,.0f}")

print("\n" + "=" * 70)
print("EJERCICIO 21 COMPLETADO")
print("=" * 70)
