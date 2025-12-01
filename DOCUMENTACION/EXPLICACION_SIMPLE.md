# 📖 GUÍA SIMPLE: Web Scraping Explicado para Principiantes

## ¿Qué es Web Scraping?

**Web Scraping = Descargar información de internet de forma automática**

Imagina que quieres extraer todos los precios de computadoras de un sitio web. En vez de copiar uno por uno, escribes un programa que lo hace por ti.

---

## Paso 1: Las 4 Librerías Que Necesitas

```python
import requests          # Para descargar páginas web
from bs4 import BeautifulSoup  # Para leer el HTML
import csv              # Para guardar en formato Excel
import json             # Para guardar en formato JSON
```

### ¿Para qué sirve cada una?

| Librería | Función | Ejemplo |
|----------|---------|---------|
| **requests** | Descargar páginas | `requests.get(url)` |
| **BeautifulSoup** | Leer HTML fácilmente | `soup.find('h1')` |
| **csv** | Guardar como Excel | `writer.writerow(datos)` |
| **json** | Guardar como JSON | `json.dump(datos)` |

---

## Paso 2: Descargar una Página Web

```python
import requests

# Decir quiénes somos (algunos sitios lo piden)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

# Descargar la página
url = 'https://ejemplo.com'
respuesta = requests.get(url, headers=headers)

# respuesta.text contiene TODO el código HTML
html = respuesta.text
```

**¿Qué pasa?**
1. Conectamos a la URL
2. Descargamos el HTML (el código de la página)
3. Lo guardamos en la variable `html`

---

## Paso 3: Leer el HTML con BeautifulSoup

```python
from bs4 import BeautifulSoup

# Convertir el HTML en algo legible
soup = BeautifulSoup(html, 'html.parser')
```

**¿Por qué?** El HTML es un texto complicado. BeautifulSoup lo convierte en algo que podemos entender y buscar.

---

## Paso 4: Buscar Elementos (LOS MÁS USADOS)

### Buscar por ETIQUETA

```python
# Encontrar el PRIMER <h1>
titulo = soup.find('h1')
print(titulo.text)  # Imprimir el texto

# Encontrar TODOS los <p>
parrafos = soup.find_all('p')
for p in parrafos:
    print(p.text)
```

### Buscar por CLASE

```html
<!-- En el HTML: -->
<div class="contenido">Hola</div>
```

```python
# En Python:
div = soup.find('div', class_='contenido')
print(div.text)  # Imprime: Hola
```

### Buscar por ID

```html
<!-- En el HTML: -->
<div id="principal">Contenido</div>
```

```python
# En Python:
div = soup.find('div', id='principal')
print(div.text)  # Imprime: Contenido
```

### Obtener Atributos

```html
<!-- En el HTML: -->
<a href="https://google.com">Google</a>
```

```python
# En Python:
enlace = soup.find('a')
url = enlace.get('href')
print(url)  # Imprime: https://google.com
```

---

## Paso 5: Ejemplo Completo Paso a Paso

### HTML de ejemplo:

```html
<div class="producto">
    <h2>Laptop</h2>
    <span class="precio">$500</span>
</div>
<div class="producto">
    <h2>Mouse</h2>
    <span class="precio">$20</span>
</div>
```

### Código Python:

```python
from bs4 import BeautifulSoup

html = """
<div class="producto">
    <h2>Laptop</h2>
    <span class="precio">$500</span>
</div>
<div class="producto">
    <h2>Mouse</h2>
    <span class="precio">$20</span>
</div>
"""

# 1. Parsear el HTML
soup = BeautifulSoup(html, 'html.parser')

# 2. Encontrar todos los productos
productos = soup.find_all('div', class_='producto')

# 3. Para cada producto, extraer datos
for producto in productos:
    nombre = producto.find('h2').text
    precio = producto.find('span', class_='precio').text
    
    print(f"Nombre: {nombre}")
    print(f"Precio: {precio}")
    print()
```

**Salida:**
```
Nombre: Laptop
Precio: $500

Nombre: Mouse
Precio: $20
```

---

## Paso 6: Guardar Datos en CSV

```python
import csv

datos = [
    {'nombre': 'Laptop', 'precio': '500'},
    {'nombre': 'Mouse', 'precio': '20'},
]

# Abrir archivo para escribir
with open('productos.csv', 'w', newline='', encoding='utf-8') as f:
    # Crear escritor
    escritor = csv.DictWriter(f, fieldnames=['nombre', 'precio'])
    
    # Escribir encabezados
    escritor.writeheader()
    
    # Escribir datos
    escritor.writerows(datos)

print("✓ Archivo guardado como productos.csv")
```

**Resultado (productos.csv):**
```
nombre,precio
Laptop,500
Mouse,20
```

---

## Paso 7: Guardar Datos en JSON

```python
import json

datos = [
    {'nombre': 'Laptop', 'precio': '500'},
    {'nombre': 'Mouse', 'precio': '20'},
]

# Guardar en JSON
with open('productos.json', 'w', encoding='utf-8') as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)

print("✓ Archivo guardado como productos.json")
```

**Resultado (productos.json):**
```json
[
  {
    "nombre": "Laptop",
    "precio": "500"
  },
  {
    "nombre": "Mouse",
    "precio": "20"
  }
]
```

---

## Paso 8: Ejemplo REAL (Descarga de un sitio)

```python
import requests
from bs4 import BeautifulSoup
import csv

# 1. Descargar la página
url = 'https://ejemplo.com/noticias'
headers = {'User-Agent': 'Mozilla/5.0'}
respuesta = requests.get(url, headers=headers)
html = respuesta.text

# 2. Parsear
soup = BeautifulSoup(html, 'html.parser')

# 3. Extraer datos
noticias = []
for articulo in soup.find_all('div', class_='articulo'):
    titulo = articulo.find('h2').text
    enlace = articulo.find('a')['href']
    
    noticias.append({
        'titulo': titulo,
        'enlace': enlace
    })

# 4. Guardar
with open('noticias.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['titulo', 'enlace'])
    writer.writeheader()
    writer.writerows(noticias)

print(f"✓ Se extrajeron {len(noticias)} noticias")
```

---

## 🔍 Los 5 Selectores Más Usados

```python
# 1. Por ETIQUETA (primer elemento)
soup.find('h1')

# 2. TODOS los de un tipo
soup.find_all('p')

# 3. Por CLASE
soup.find('div', class_='contenido')

# 4. Por ID
soup.find('div', id='principal')

# 5. Obtener ATRIBUTO
elemento['href']  o  elemento.get('href')
```

---

## ⚠️ Errores Comunes

### Error 1: Elemento no encontrado
```python
# ✗ Esto falla si no existe
titulo = soup.find('h1').text

# ✓ Forma segura:
titulo_elem = soup.find('h1')
if titulo_elem:
    titulo = titulo_elem.text
else:
    titulo = "No encontrado"
```

### Error 2: Falta de encoding
```python
# ✓ Siempre usar encoding
with open('datos.csv', 'w', encoding='utf-8') as f:
    ...
```

### Error 3: No esperar a que cargue
```python
# Si la página tiene JavaScript, requests no lo carga
# En ese caso necesitas Selenium (más complejo)
```

---

## 📋 RESUMEN - Lo Más Importante

```python
# PASO 1: Importar
import requests
from bs4 import BeautifulSoup

# PASO 2: Descargar
respuesta = requests.get(url)
html = respuesta.text

# PASO 3: Parsear
soup = BeautifulSoup(html, 'html.parser')

# PASO 4: Extraer
elementos = soup.find_all('div', class_='item')
for elem in elementos:
    titulo = elem.find('h2').text
    print(titulo)

# PASO 5: Guardar
import csv
with open('datos.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['titulo'])
    writer.writerow([titulo])
```

---

## 📝 Ejercicio Práctico

Ejecuta esto:
```bash
python ejercicio19_simple.py
```

Verás:
1. Cómo extraer noticias
2. Cómo extraer productos
3. Cómo guardar en CSV y JSON
4. Los 5 selectores explicados

---

## 🎯 Antes de Empezar en INTERNET

**IMPORTANTE - Lee siempre:**

1. ✓ Revisa si el sitio tiene una **API oficial** (mejor opción)
2. ✓ Lee el archivo `robots.txt` (https://ejemplo.com/robots.txt)
3. ✓ Revisa los **términos de servicio**
4. ✓ Agrega **delays** entre descargas (`time.sleep(2)`)
5. ✓ Usa un **User-Agent** realista
6. ✓ **NO sobrecarges** el servidor

---

## 💡 Próximos Pasos

1. Corre `ejercicio19_simple.py` y entiende el código
2. Abre los archivos generados (CSV y JSON)
3. Modifica el código para extraer OTROS datos
4. Intenta con un sitio REAL (respetando reglas)
5. Si el sitio tiene JavaScript, aprende **Selenium**

---

**¡Eso es todo! Web Scraping es solo:
Descargar → Leer → Extraer → Guardar**
