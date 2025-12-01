# 📖 GUÍA RÁPIDA - Web Scraping en Python

## 🚀 Inicio Rápido

```python
# 1. Descargar página
import requests
from bs4 import BeautifulSoup

url = 'https://ejemplo.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 2. Buscar elementos
titulo = soup.find('h1')                           # Primer elemento
articulos = soup.find_all('article')              # Todos los elementos
por_clase = soup.find('div', class_='contenido')  # Por clase
por_id = soup.find('div', id='principal')         # Por ID

# 3. Extraer texto y atributos
print(titulo.text)                # Texto del elemento
print(articulo['href'])           # Atributo específico
print(articulo.get('data-id'))   # get() si puede no existir

# 4. Guardar datos
import csv, json

# CSV
with open('datos.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['nombre', 'precio'])
    writer.writeheader()
    writer.writerows(datos)

# JSON
with open('datos.json', 'w') as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)
```

## 🎯 Selectores CSS - Cheat Sheet

```python
# BÁSICOS
soup.find('h1')                          # Etiqueta
soup.find('div', class_='content')       # Clase
soup.find('div', id='main')              # ID
soup.find_all('p')                       # Todos

# CSS SELECTORS
soup.select('.clase')                    # Por clase
soup.select('#id')                       # Por ID
soup.select('div > p')                   # Hijo directo
soup.select('div p')                     # Descendiente
soup.select('.padre.hijo')               # Múltiples clases
soup.select('[href]')                    # Con atributo
soup.select('a[href="url"]')             # Atributo específico

# BÚSQUEDA POR ATRIBUTO
soup.find('a', {'data-id': '123'})
soup.find('img', attrs={'src': True})

# TEXTO
soup.find(string='exacto')
soup.find(string=re.compile('patrón'))
```

## ⚡ Patrones Comunes

### Paginación
```python
for pagina in range(1, 6):
    url = f'https://ejemplo.com?page={pagina}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Procesar datos...
    time.sleep(2)  # ⚠️ Respetar servidor
```

### Manejo de Errores
```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error: {e}")
```

### Headers Realistas
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}
response = requests.get(url, headers=headers)
```

### Tabla HTML → DataFrame
```python
import pandas as pd

# Opción 1: Directo
df = pd.read_html(url)[0]

# Opción 2: Manual
import csv
soup = BeautifulSoup(html, 'html.parser')
filas = []
for tr in soup.find_all('tr'):
    celdas = [td.text for td in tr.find_all('td')]
    filas.append(celdas)
```

### Multi-threading
```python
from threading import Thread
from queue import Queue

def worker():
    while not queue.empty():
        url = queue.get()
        response = requests.get(url)
        # Procesar...

queue = Queue()
for url in urls:
    queue.put(url)

threads = [Thread(target=worker) for _ in range(5)]
for t in threads:
    t.start()
```

### Reintentos Automáticos
```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

response = session.get(url)
```

## 🧹 Limpieza de Datos

```python
import re

# Espacios extras
texto = re.sub(r'\s+', ' ', texto.strip())

# Números
numeros = re.findall(r'\d+\.?\d*', texto)

# Email
email_valido = re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

# URL
url_valida = re.match(r'^https?://[\w\.-]+\.\w+', url)

# Remover HTML
texto_limpio = re.sub(r'<[^>]+>', '', html)
```

## 📊 Análisis con Pandas

```python
import pandas as pd

# Crear
df = pd.DataFrame(datos)

# Estadísticas
df['precio'].mean()     # Promedio
df['precio'].max()      # Máximo
df['precio'].min()      # Mínimo
df['stock'].sum()       # Total

# Filtrar
baratos = df[df['precio'] < 100]

# Agrupar
df.groupby('categoría').agg({
    'precio': 'mean',
    'stock': 'sum'
})

# Guardar
df.to_csv('datos.csv', index=False)
df.to_json('datos.json')
```

## ⚠️ Buenas Prácticas

| ✓ SÍ | ✗ NO |
|------|------|
| Agregar delays | Requests sin parar |
| User-Agent real | Identificarse como bot |
| Respetar robots.txt | Ignorar restricciones |
| Manejo errores | Crashes silenciosos |
| Limitar velocidad | DoS accidental |
| APIs primero | Siempre scraping |
| Validar datos | Guardar sin revisar |
| Logging detallado | Sin registros |

## 🌐 Selenium para JavaScript

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://ejemplo.com')

# Esperar elemento
elemento = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "contenido"))
)

# Extraer
items = driver.find_elements(By.CLASS_NAME, "item")
for item in items:
    print(item.text)

# Acciones
elemento.click()
elemento.send_keys('texto')
driver.scroll_into_view(elemento)

driver.quit()
```

## 🐛 Troubleshooting

| Error | Causa | Solución |
|-------|-------|----------|
| 403 Forbidden | Bot detectado | Agregar User-Agent |
| Timeout | Servidor lento | Aumentar timeout |
| Elemento no existe | Selector incorrecto | Revisar selector |
| Contenido dinámico | JavaScript | Usar Selenium |
| IP bloqueada | Muchos requests | Usar delays, VPN |
| Caracteres extraños | Encoding | Verificar charset |

## 📚 Recursos

```python
# Instalar
pip install requests beautifulsoup4 lxml selenium pandas

# Útiles
soup.prettify()              # Ver HTML formateado
soup.get_text()             # Todo el texto
soup.decompose()            # Remover elemento
soup.extract()              # Remover y retornar
soup.replace_with('nuevo')  # Reemplazar

# Debugging
print(soup.prettify())
print(response.status_code)
print(response.headers)
```

## 🎓 Ejemplo Completo

```python
import requests
from bs4 import BeautifulSoup
import csv
import time

# Descargar
url = 'https://ejemplo.com/productos'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers, timeout=10)

# Parsear
soup = BeautifulSoup(response.content, 'html.parser')

# Extraer
datos = []
for item in soup.find_all('div', class_='producto'):
    nombre = item.find('h2').text.strip()
    precio = float(item.find('span', class_='precio').text.replace('$', ''))
    datos.append({'nombre': nombre, 'precio': precio})

# Guardar
with open('productos.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['nombre', 'precio'])
    writer.writeheader()
    writer.writerows(datos)

print(f"✓ {len(datos)} productos extraídos")
```

## 📋 Checklist Antes de Scrapear

- [ ] ¿Revisar términos de servicio?
- [ ] ¿API disponible?
- [ ] ¿Permitido en robots.txt?
- [ ] ¿Agregar delays?
- [ ] ¿User-Agent realista?
- [ ] ¿Manejo de errores?
- [ ] ¿Logging habilitado?
- [ ] ¿Datos validados?

---

**Consejos Finales:**
1. Siempre prueba en pequeña escala primero
2. Guarda el HTML para debugging
3. Respeta el servidor remoto
4. Mantén un log de cambios
5. Valida los datos extraídos
6. Considera usar APIs primero
7. Documental tu código
8. Ten plan B si el sitio cambia
