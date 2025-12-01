# Ejercicio 19: Web Scraping - Extracción de Datos Web

## 📚 ¿Qué es Web Scraping?

Web scraping es la técnica de extraer datos de sitios web de forma automatizada. Es útil para:
- Recopilar precios de productos
- Extraer noticias y artículos
- Obtener información de mercado
- Analizar datos de redes sociales
- Investigación de mercado
- Monitoreo de cambios en sitios web

## 🔧 ¿Cómo Funciona?

Python descarga el HTML de una página web, lo analiza usando bibliotecas como BeautifulSoup, encuentra elementos específicos y extrae la información deseada.

**Flujo básico:**
1. Descargar HTML con `requests`
2. Parsear con `BeautifulSoup`
3. Buscar elementos con selectores CSS/XPath
4. Extraer datos
5. Guardar en CSV/JSON/DB

## 📦 Librerías Principales

| Librería | Función |
|----------|---------|
| `requests` | Descargar páginas web |
| `BeautifulSoup` | Analizar HTML/XML |
| `lxml` | Parser rápido de HTML |
| `selenium` | Automatizar navegadores (JS) |
| `scrapy` | Framework completo |
| `pandas` | Procesar datos extraídos |

## 📁 Archivos Incluidos

### 1. **ejercicio19.py** - Sistema Básico
Incluye:
- ✓ Extracción de noticias
- ✓ Scraping de precios
- ✓ Análisis de tablas HTML
- ✓ Selectores CSS avanzados
- ✓ Análisis con Pandas
- ✓ Expresiones regulares
- ✓ Exportación a CSV/JSON

**Archivo generados:**
- `noticias.csv` / `noticias.json`
- `productos.csv` / `productos.json`
- `tabla_datos.csv` / `tabla_datos.json`
- `selectores_css.json`

### 2. **ejercicio19b.py** - Sistema Avanzado
Incluye:
- ✓ Selenium para sitios dinámicos
- ✓ Patrones de paginación
- ✓ Autenticación (login)
- ✓ Manejo robusto de errores
- ✓ Multi-threading
- ✓ Cacheo de datos
- ✓ Mejores prácticas

## 🚀 Instalación y Uso

### 1. Instalar dependencias
```bash
pip install requests beautifulsoup4 lxml selenium pandas
```

### 2. Ejecutar ejercicio básico
```bash
python ejercicio19.py
```

### 3. Ejecutar ejercicio avanzado
```bash
python ejercicio19b.py
```

### 4. Para usar Selenium (opcional)
```bash
# Descargar ChromeDriver desde:
# https://chromedriver.chromium.org/
# Colocar en PATH o especificar ruta
```

## 📝 Ejemplos de Código

### Ejemplo Básico: Extraer Noticias

```python
import requests
from bs4 import BeautifulSoup

# Descargar página
response = requests.get('https://ejemplo.com')
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar todos los artículos
articulos = soup.find_all('article')

# Extraer información
for articulo in articulos:
    titulo = articulo.find('h2').text
    enlace = articulo.find('a')['href']
    print(f"{titulo}: {enlace}")
```

### Ejemplo: Selectores CSS

```python
# Por etiqueta
soup.find('h1')

# Por clase
soup.find('div', class_='contenido')

# Por ID
soup.find('div', id='principal')

# Selector CSS combinado
soup.select('.clase #id')

# Todos los elementos de un tipo
soup.find_all('a')

# Obtener atributos
elemento['href']
elemento.get('src')
```

### Ejemplo: Tablas HTML

```python
import pandas as pd

# Leer tabla directamente
tabla = pd.read_html('https://ejemplo.com/tabla.html')[0]

# O manualmente
filas = soup.find_all('tr')
datos = []
for fila in filas:
    celdas = [celda.text for celda in fila.find_all('td')]
    datos.append(celdas)
```

### Ejemplo: Guardar Datos

```python
import csv
import json

# Guardar CSV
with open('datos.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['titulo', 'precio'])
    writer.writeheader()
    writer.writerows(datos)

# Guardar JSON
with open('datos.json', 'w') as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)
```

## 🎯 Selectores CSS - Referencia Rápida

```python
# Por etiqueta
soup.find('h1')

# Por clase única
soup.find('div', class_='contenido')

# Por múltiples clases
soup.select('.class1.class2')

# Por ID
soup.find('div', id='principal')

# CSS selector descendiente
soup.select('.padre .hijo')

# CSS selector hijo directo
soup.select('.padre > .hijo')

# Atributo específico
soup.find('a', {'data-id': '123'})

# Por patrón de atributo
soup.find_all('a', href=True)

# Clase contenga texto
soup.find_all(string='texto')

# Múltiples elementos
soup.find_all(['h1', 'h2', 'h3'])
```

## 🛡️ Buenas Prácticas

### 1. **Respetar Limits**
```python
import time

# Añadir delays entre requests
for url in urls:
    response = requests.get(url)
    time.sleep(2)  # Esperar 2 segundos
```

### 2. **Headers Realistas**
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
response = requests.get(url, headers=headers)
```

### 3. **Manejo de Errores**
```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    logging.error(f"Error: {e}")
```

### 4. **Verificar robots.txt**
```python
# Siempre revisar https://ejemplo.com/robots.txt
# Respetar Disallow y crawl-delay
```

### 5. **Reintentos Automáticos**
```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
```

## ⚠️ Consideraciones Legales

- ✓ Verificar **términos de servicio** del sitio
- ✓ Respetar **copyright** de contenidos
- ✓ No sobrecargar servidores
- ✓ Considerar **APIs oficiales** primero
- ✓ Revisar **robots.txt**
- ✓ Usar solo para propósitos legales
- ✓ Creditar al autor original si necesario

## 🔍 Expresiones Regulares

```python
import re

# Extraer números
numeros = re.findall(r'\d+\.?\d*', 'Precio: $999.99')
# Resultado: ['999', '99']

# Validar email
patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
bool(re.match(patron, 'usuario@ejemplo.com'))  # True

# Limpiar espacios extras
texto_limpio = re.sub(r'\s+', ' ', texto.strip())

# Extraer URLs
urls = re.findall(r'https?://\S+', 'Visit https://ejemplo.com')
```

## 📊 Análisis con Pandas

```python
import pandas as pd

# Crear DataFrame
df = pd.DataFrame(datos)

# Estadísticas básicas
print(df['precio'].mean())     # Promedio
print(df['precio'].max())      # Máximo
print(df['stock'].sum())       # Total

# Agrupar datos
df.groupby('categoría').agg({
    'precio': 'mean',
    'stock': 'sum'
})

# Filtrar
baratos = df[df['precio'] < 100]

# Guardar
df.to_csv('datos.csv', index=False)
```

## 🌐 Selenium para Sitios Dinámicos

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar driver
driver = webdriver.Chrome()

# Cargar página
driver.get('https://ejemplo.com')

# Esperar elemento
elemento = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "elemento"))
)

# Extraer información
datos = driver.find_elements(By.CLASS_NAME, "item")
for item in datos:
    print(item.text)

# Cerrar
driver.quit()
```

## 🏗️ Patrones Avanzados

### Paginación
```python
for pagina in range(1, 5):
    url = f"https://ejemplo.com?page={pagina}"
    response = requests.get(url)
    # Procesar datos...
    time.sleep(2)
```

### Autenticación
```python
session = requests.Session()
session.post('https://ejemplo.com/login', data={
    'username': 'usuario',
    'password': 'contraseña'
})
response = session.get('https://ejemplo.com/protegido')
```

### Multi-threading
```python
from threading import Thread
from queue import Queue

queue = Queue()
for url in urls:
    queue.put(url)

def worker():
    while not queue.empty():
        url = queue.get()
        # Procesar...

threads = [Thread(target=worker) for _ in range(5)]
for t in threads:
    t.start()
```

## 📈 Comparativa de Herramientas

| Aspecto | requests+BS4 | Selenium | Scrapy |
|---------|-------------|----------|--------|
| Velocidad | ⚡⚡⚡ | ⚡ | ⚡⚡ |
| Curva aprendizaje | 🟢 | 🟡 | 🔴 |
| JavaScript | ❌ | ✅ | Plugins |
| Proyecto pequeño | ✅ | ✅ | ❌ |
| Proyecto grande | 🟡 | 🟡 | ✅ |
| Mantenimiento | 🟢 | 🟡 | ❌ |

## 🐛 Troubleshooting

| Problema | Solución |
|----------|----------|
| 403 Forbidden | Agregar User-Agent realista |
| Timeout | Aumentar timeout y agregar reintentos |
| Elementos no encontrados | Verificar selectores, esperar carga |
| IP bloqueada | Usar proxies, VPN, esperar |
| Datos dinámicos | Usar Selenium o verificar XHR |

## 📚 Recursos Útiles

- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/)
- [Requests Docs](https://requests.readthedocs.io/)
- [Selenium Docs](https://selenium.dev/)
- [Scrapy Docs](https://scrapy.org/)
- [Regex Tester](https://regex101.com/)

## ✅ Checklist para Web Scraping

- [ ] Revisar términos de servicio
- [ ] Verificar robots.txt
- [ ] Agregar User-Agent
- [ ] Implementar delays
- [ ] Manejar errores
- [ ] Usar try-except
- [ ] Registrar actividad (logging)
- [ ] Validar datos extraídos
- [ ] Respetar crawl-delay
- [ ] Considerar alternativas (APIs)

## 🎓 Resumen

Web scraping es una herramienta poderosa para recopilar datos, pero debe usarse responsablemente:

1. **Siempre respetar** los términos de servicio
2. **No sobrecargar** servidores
3. **Preferir APIs** cuando estén disponibles
4. **Manejar errores** adecuadamente
5. **Usar datos** de forma legal y ética

---

**Versión:** 1.0  
**Fecha:** 2025-12-01  
**Autor:** Ejercicio Python 19  
**Nivel:** Intermedio-Avanzado
