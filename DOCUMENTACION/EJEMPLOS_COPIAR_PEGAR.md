# 🎯 COPIAR Y PEGAR: Ejemplos Listos para Usar

## Ejemplo 1: Extraer Títulos

**Problema:** Quiero extraer todos los títulos (h1, h2, h3) de una página

```python
import requests
from bs4 import BeautifulSoup

# Descargar página
url = 'https://ejemplo.com'
respuesta = requests.get(url)
html = respuesta.text

# Parsear
soup = BeautifulSoup(html, 'html.parser')

# Extraer títulos
titulos = soup.find_all('h1')
for titulo in titulos:
    print(titulo.text)
```

---

## Ejemplo 2: Extraer Enlaces

**Problema:** Quiero todos los enlaces (links)

```python
import requests
from bs4 import BeautifulSoup

url = 'https://ejemplo.com'
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, 'html.parser')

# Encontrar todos los enlaces
enlaces = soup.find_all('a')

for enlace in enlaces:
    # Obtener el texto del enlace
    texto = enlace.text
    # Obtener la URL
    url_enlace = enlace.get('href')
    
    print(f"{texto}: {url_enlace}")
```

---

## Ejemplo 3: Extraer de una Tabla

**Problema:** Extraer datos de una tabla HTML

```python
import requests
from bs4 import BeautifulSoup

url = 'https://ejemplo.com'
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, 'html.parser')

# Encontrar la tabla
tabla = soup.find('table')

# Extraer cada fila
for fila in tabla.find_all('tr'):
    # Extraer celdas
    celdas = fila.find_all('td')
    
    # Imprimir cada celda
    for celda in celdas:
        print(celda.text, end=" | ")
    print()  # Nueva línea
```

---

## Ejemplo 4: Extraer Información de Productos

**Problema:** Extraer nombre y precio de cada producto

```python
import requests
from bs4 import BeautifulSoup

url = 'https://tienda.ejemplo.com'
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, 'html.parser')

# Encontrar todos los productos
productos = soup.find_all('div', class_='producto')

for producto in productos:
    # Extraer nombre
    nombre = producto.find('h2').text
    
    # Extraer precio
    precio = producto.find('span', class_='precio').text
    
    print(f"{nombre} - {precio}")
```

---

## Ejemplo 5: Guardar en CSV (Excel)

**Problema:** Quiero guardar los datos en un archivo Excel

```python
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://tienda.ejemplo.com'
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, 'html.parser')

# Extraer productos
datos = []
for producto in soup.find_all('div', class_='producto'):
    nombre = producto.find('h2').text
    precio = producto.find('span', class_='precio').text
    
    datos.append({'nombre': nombre, 'precio': precio})

# Guardar en CSV
with open('productos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['nombre', 'precio'])
    writer.writeheader()
    writer.writerows(datos)

print("✓ Guardado en productos.csv")
```

---

## Ejemplo 6: Guardar en JSON

**Problema:** Quiero guardar en formato JSON

```python
import requests
from bs4 import BeautifulSoup
import json

url = 'https://tienda.ejemplo.com'
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, 'html.parser')

# Extraer productos
datos = []
for producto in soup.find_all('div', class_='producto'):
    nombre = producto.find('h2').text
    precio = producto.find('span', class_='precio').text
    
    datos.append({'nombre': nombre, 'precio': precio})

# Guardar en JSON
with open('productos.json', 'w', encoding='utf-8') as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)

print("✓ Guardado en productos.json")
```

---

## Ejemplo 7: Con Manejo de Errores

**Problema:** El código falla si algo no existe

```python
import requests
from bs4 import BeautifulSoup

url = 'https://ejemplo.com'

try:
    respuesta = requests.get(url, timeout=5)
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    
    # Extraer productos
    productos = soup.find_all('div', class_='producto')
    
    for producto in productos:
        # Buscar elemento
        nombre_elem = producto.find('h2')
        if nombre_elem:
            nombre = nombre_elem.text
        else:
            nombre = "Sin nombre"
        
        # Buscar precio
        precio_elem = producto.find('span', class_='precio')
        if precio_elem:
            precio = precio_elem.text
        else:
            precio = "Sin precio"
        
        print(f"{nombre} - {precio}")

except Exception as e:
    print(f"✗ Error: {e}")
```

---

## Ejemplo 8: Limpiar Espacios Extras

**Problema:** El texto tiene espacios raros

```python
import requests
from bs4 import BeautifulSoup

url = 'https://ejemplo.com'
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, 'html.parser')

# Extraer elementos
for titulo in soup.find_all('h2'):
    # Limpiar espacios
    texto = titulo.text.strip()
    
    # Quitar espacios extras
    import re
    texto_limpio = re.sub(r'\s+', ' ', texto)
    
    print(texto_limpio)
```

---

## Ejemplo 9: Descargar Varias Páginas

**Problema:** Quiero extraer de múltiples páginas

```python
import requests
from bs4 import BeautifulSoup
import time

for pagina in range(1, 4):  # Páginas 1, 2, 3
    url = f'https://ejemplo.com?page={pagina}'
    
    respuesta = requests.get(url)
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    
    # Extraer datos
    for producto in soup.find_all('div', class_='producto'):
        nombre = producto.find('h2').text
        print(f"Página {pagina}: {nombre}")
    
    # Esperar 2 segundos (ser respetuoso)
    time.sleep(2)
```

---

## Ejemplo 10: Con Identificación (Headers)

**Problema:** El sitio me bloquea

```python
import requests
from bs4 import BeautifulSoup

# Headers para parecer un navegador normal
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

url = 'https://ejemplo.com'
respuesta = requests.get(url, headers=headers)
soup = BeautifulSoup(respuesta.text, 'html.parser')

# Ahora es más probable que funcione
print("✓ Conectado")
```

---

## ⚙️ Template Base (Copia esto)

```python
import requests
from bs4 import BeautifulSoup
import csv
import json

# Configuración
URL = 'https://ejemplo.com'
ARCHIVO_CSV = 'datos.csv'
ARCHIVO_JSON = 'datos.json'

# Headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

# Descargar
print("Descargando...")
respuesta = requests.get(URL, headers=headers)
html = respuesta.text

# Parsear
print("Parseando...")
soup = BeautifulSoup(html, 'html.parser')

# Extraer
print("Extrayendo...")
datos = []
for elemento in soup.find_all('div', class_='item'):
    # MODIFICA ESTO según lo que necesites
    nombre = elemento.find('h2').text.strip()
    precio = elemento.find('span', class_='precio').text.strip()
    
    datos.append({'nombre': nombre, 'precio': precio})

# Guardar CSV
print("Guardando CSV...")
with open(ARCHIVO_CSV, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['nombre', 'precio'])
    writer.writeheader()
    writer.writerows(datos)

# Guardar JSON
print("Guardando JSON...")
with open(ARCHIVO_JSON, 'w', encoding='utf-8') as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)

print(f"✓ Hecho! Se extrajeron {len(datos)} elementos")
```

---

## 🔑 Claves Importantes

**Siempre:**
```python
# Usar headers
headers = {'User-Agent': 'Mozilla/5.0...'}

# Encoding UTF-8
encoding='utf-8'

# Espacios en blanco
.strip()  # Quita espacios

# Manejo de errores
try:
    ...
except Exception as e:
    print(e)
```

---

## ❌ Errores Comunes

```python
# ✗ MAL: Sin encoding
with open('datos.csv', 'w') as f:

# ✓ BIEN:
with open('datos.csv', 'w', encoding='utf-8') as f:

# ✗ MAL: Sin strip()
titulo = elemento.find('h2').text

# ✓ BIEN:
titulo = elemento.find('h2').text.strip()

# ✗ MAL: Sin try-except
precio = float(precio_texto)

# ✓ BIEN:
try:
    precio = float(precio_texto)
except:
    precio = 0
```

---

¡Eso es todo! Copia, adapta y usa 🚀
