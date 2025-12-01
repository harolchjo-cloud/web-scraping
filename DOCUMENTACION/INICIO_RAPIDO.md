# 🚀 INICIO RÁPIDO - Ejercicio 19: Web Scraping

## ⚡ En 3 Pasos

### 1️⃣ Instalar (una sola vez)
```bash
pip install requests beautifulsoup4 lxml selenium pandas
```

### 2️⃣ Ejecutar
```bash
# Sistema básico
python ejercicio19.py

# Sistema avanzado  
python ejercicio19b.py

# Ejemplos prácticos
python ejercicio19c.py
```

### 3️⃣ Ver resultados
```bash
# Ver datos extraídos
type noticias.json
type productos.csv

# O abre los archivos en editor
```

---

## 📋 ¿Qué Archivo Leer?

### **Quiero...**

🟢 **Empezar rápido**  
→ Lee: `GUIA_RAPIDA_WebScraping.md` (5 minutos)  
→ Ejecuta: `python ejercicio19.py`

🟡 **Entender profundamente**  
→ Lee: `README_WebScraping.md` (30 minutos)  
→ Ejecuta: Los 3 scripts en orden

🔴 **Aprender patrones avanzados**  
→ Lee: `ejercicio19b.py` (código comentado)  
→ Ejecuta: `python ejercicio19b.py`

🟣 **Usar en mi proyecto**  
→ Copia: Clases de `ejercicio19c.py`  
→ Lee: Docstrings de cada clase

---

## 📚 Estructura de Aprendizaje

```
NIVEL 1: Básico (15-20 min)
├── Leer: GUIA_RAPIDA_WebScraping.md (primeras 5 secciones)
├── Ver: ejercicio19.py (estructura principal)
└── Ejecutar: python ejercicio19.py

NIVEL 2: Intermedio (30-45 min)
├── Leer: README_WebScraping.md (completo)
├── Ver: ejercicio19c.py (clases reutilizables)
└── Entender: Patrones de limpieza y validación

NIVEL 3: Avanzado (45-60 min)
├── Leer: ejercicio19b.py (comentarios)
├── Ver: PatronesAvanzados y MejoresPracticas
└── Ejecutar: python ejercicio19b.py
```

---

## 🎯 Casos de Uso Rápidos

### Extraer títulos y enlaces
```python
import requests
from bs4 import BeautifulSoup

url = 'https://ejemplo.com'
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')

# Extraer
for articulo in soup.find_all('article'):
    titulo = articulo.find('h2').text
    enlace = articulo.find('a')['href']
    print(f"{titulo}: {enlace}")
```

### Extraer tabla
```python
import pandas as pd

# Opción 1: Directo
df = pd.read_html('https://ejemplo.com/tabla.html')[0]

# Opción 2: Manual
filas = soup.find_all('tr')
datos = []
for fila in filas:
    datos.append([td.text for td in fila.find_all('td')])
```

### Guardar datos
```python
import json

# JSON
with open('datos.json', 'w', encoding='utf-8') as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)

# CSV
df.to_csv('datos.csv', index=False)
```

---

## ⚠️ Recuerda Siempre

✅ **Haz:**
- Revisar términos de servicio
- Agregar delays (`time.sleep(2)`)
- Usar User-Agent realista
- Manejar errores

❌ **No hagas:**
- Sobrecargar servidores
- Ignorar robots.txt
- Extraer datos personales
- Violar copyright

---

## 🔍 Selectores Comunes

```python
soup.find('h1')                      # Primer h1
soup.find_all('p')                   # Todos los p
soup.find('div', class_='content')   # Por clase
soup.find('div', id='main')          # Por ID
soup.select('.content > p')          # CSS selector
soup.find_all(string='texto')        # Por texto
```

---

## 📊 Datos Generados

Después de ejecutar, tendrás:
- **noticias.csv/json** - 3 noticias de ejemplo
- **productos.csv/json** - 3 productos con precios
- **tabla_datos.csv/json** - 3 países con datos
- **scraping.log** - Log de eventos

---

## 🚫 Problemas Comunes

| Problema | Solución |
|----------|----------|
| `ModuleNotFoundError` | `pip install` las librerías |
| `403 Forbidden` | Agregar User-Agent en headers |
| Elemento no encontrado | Verificar selector CSS |
| Timeout | Aumentar timeout, agregar reintentos |

---

## 💡 Próximo Paso

1. Ejecuta los 3 scripts
2. Lee GUIA_RAPIDA_WebScraping.md
3. Modifica un script para tu caso
4. Estudia README_WebScraping.md
5. ¡Crea tu propio scraper!

---

**¡Listo para empezar! 🎉**
