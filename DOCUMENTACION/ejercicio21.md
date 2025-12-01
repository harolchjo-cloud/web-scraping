# Ejercicio 21: Machine Learning Básico - Predicciones con Scikit-Learn

## ¿Qué es y para qué sirve?
Machine Learning permite que las computadoras aprendan patrones de los datos sin ser programadas explícitamente. Scikit-learn es la biblioteca más popular para ML en Python, ideal para clasificación, regresión, clustering y más.

## ¿Cómo funciona?
Los algoritmos de ML analizan datos históricos para encontrar patrones y hacer predicciones sobre datos nuevos. Es como enseñar a una computadora a reconocer patrones igual que lo haría un humano, pero procesando miles de ejemplos.

## Contenido del ejercicio

### Archivos
- `ejercicio21.py` - Sistema completo de ML con múltiples modelos
- `dataset_casas.csv` - Dataset de ejemplo (precios de casas)
- `ml_visualizaciones.png` - Gráficos generados (se crea al ejecutar)

### Modelos incluidos

1. **Regresión Lineal** - Predecir valores numéricos (precios)
2. **Clasificación Logística** - Clasificación binaria (casa cara/barata)
3. **Random Forest** - Múltiples árboles de decisión
4. **K-Means** - Agrupamiento no supervisado (clustering)
5. **Validación Cruzada** - Evaluar generalización del modelo

## Explicación línea por línea (resumen)

```python
from sklearn.model_selection import train_test_split
# Divide datos en entrenamiento (80%) y prueba (20%)

from sklearn.linear_model import LinearRegression
# Importa algoritmo de regresión lineal

model = LinearRegression()
# Crea instancia del modelo

model.fit(X_train, y_train)
# Entrena el modelo con datos de entrenamiento

predictions = model.predict(X_test)
# Hace predicciones sobre datos de prueba

from sklearn.metrics import accuracy_score
# Importa métricas de evaluación

accuracy_score(y_true, y_pred)
# Calcula precisión del modelo
```

## Algoritmos principales

### 1. Regresión Lineal
- **Uso**: Predecir valores numéricos continuos (precios, temperaturas, etc.)
- **Función**: `LinearRegression()`
- **Salida**: Valor numérico

### 2. Regresión Logística
- **Uso**: Clasificación binaria (sí/no, pasa/falla)
- **Función**: `LogisticRegression()`
- **Salida**: Probabilidad entre 0 y 1

### 3. Random Forest
- **Uso**: Múltiples árboles de decisión para mejor precisión
- **Función**: `RandomForestRegressor()`, `RandomForestClassifier()`
- **Ventaja**: Evita overfitting, maneja datos complejos

### 4. K-Means
- **Uso**: Agrupamiento no supervisado (encontrar patrones)
- **Función**: `KMeans(n_clusters=3)`
- **Salida**: Grupo/cluster asignado

### 5. SVM (Support Vector Machines)
- **Uso**: Clasificación con límites complejos
- **Función**: `SVC()` o `SVR()`

### 6. KNN (K-Nearest Neighbors)
- **Uso**: Clasificación basada en similitud
- **Función**: `KNeighborsClassifier()`

## Métricas de evaluación

### Para Regresión
- **MSE** (Mean Squared Error): Error promedio al cuadrado
- **RMSE** (Root MSE): Raíz del MSE (mismas unidades que variable objetivo)
- **R²** (Coeficiente de Determinación): 1.0 = perfecto, 0.0 = malo (rango -∞ a 1.0)
- **MAE** (Mean Absolute Error): Error promedio

### Para Clasificación
- **Accuracy** (Precisión): % de predicciones correctas
- **Precision**: De los predichos positivos, cuántos eran reales
- **Recall** (Sensibilidad): De los positivos reales, cuántos detectó
- **F1-Score**: Balance entre Precision y Recall

### Generales
- **Confusion Matrix**: Matriz de predicciones vs reales
- **Cross-Validation**: Evalúa en múltiples splits (más confiable)

## Funciones especiales útiles

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Normaliza datos: media=0, desv.std=1 (mejor rendimiento)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)
# Convierte texto a números (ej: ["rojo", "azul"] -> [0, 1])

from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(model, param_grid={'C': [0.1, 1, 10]})
grid.fit(X, y)
# Búsqueda automática de mejores parámetros

from sklearn.pipeline import Pipeline
pipe = Pipeline([('scaler', StandardScaler()), ('model', LinearRegression())])
# Encadena múltiples pasos de procesamiento

from sklearn.feature_selection import SelectKBest
selector = SelectKBest(k=5)
X_best = selector.fit_transform(X, y)
# Selecciona las k mejores características
```

## Despliegue local - pasos rápidos

### 1. Instalar dependencias
```bash
pip install scikit-learn pandas numpy matplotlib
```

### 2. Archivos necesarios
- `ejercicio21.py` - Código principal
- `dataset_casas.csv` - Dataset (ya incluido)

### 3. Ejecutar
```bash
python ejercicio21.py
```

### 4. Salida esperada
- Métricas de evaluación en consola
- Gráficos guardados en `ml_visualizaciones.png`
- Predicciones sobre nuevos datos

## Flujo típico de ML

```
1. Cargar datos
   ↓
2. Explorar y entender datos
   ↓
3. Dividir en entrenamiento/prueba
   ↓
4. Normalizar características (opcional pero recomendado)
   ↓
5. Entrenar modelo: model.fit(X_train, y_train)
   ↓
6. Predecir: y_pred = model.predict(X_test)
   ↓
7. Evaluar con métricas
   ↓
8. Ajustar parámetros si es necesario
   ↓
9. Predicción en nuevos datos
```

## Ejemplo rápido - Predicción de precios

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Cargar datos
df = pd.read_csv('dataset_casas.csv')
X = df[['tamaño', 'habitaciones', 'baños']]
y = df['precio']

# Dividir
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Entrenar
model = LinearRegression()
model.fit(X_train, y_train)

# Predicción
nueva_casa = [[150, 3, 2]]  # 150m², 3 hab, 2 baños
precio = model.predict(nueva_casa)[0]
print(f"Precio estimado: ${precio:,.0f}")
```

## Consejos prácticos

1. **Siempre** normaliza los datos (StandardScaler)
2. **Valida** con Cross-Validation, no solo train/test
3. **Prueba** múltiples modelos (compare R², Accuracy, etc.)
4. **Evita** overfitting (modelo que memoriza en lugar de aprender)
5. **Ajusta** parámetros con GridSearchCV
6. **Visualiza** resultados (scatter plots, histogramas)
7. **Documenta** tu proceso y decisiones
8. **Mantén** proporciones: 70-80% entrenamiento, 20-30% prueba

## Dataset (dataset_casas.csv)

Contiene 30 casas con características:
- **tamaño**: Área en m²
- **habitaciones**: Número de habitaciones
- **baños**: Número de baños
- **edad**: Antigüedad en años
- **precio**: Precio de venta ($)

## Requisitos mínimos

```
Python 3.7+
scikit-learn >= 1.0
pandas >= 1.0
numpy >= 1.19
matplotlib >= 3.3
```

## Recursos útiles

- [Scikit-learn docs](https://scikit-learn.org/)
- [Kaggle datasets](https://www.kaggle.com/datasets)
- [Ejemplos de modelos](https://scikit-learn.org/stable/auto_examples/)

---

¡Listo! Ejecuta `python ejercicio21.py` y verás predicciones reales de precios de casas con evaluación completa.
