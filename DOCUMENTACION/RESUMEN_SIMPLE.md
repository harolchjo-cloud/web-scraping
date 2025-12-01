# 🎓 WEB SCRAPING - RESUMEN PARA ESTUDIANTES

## ¿Qué es Web Scraping?

**Es descargar información de internet automáticamente**

Ejemplo: En vez de copiar precios uno por uno, tu código lo hace.

---

## Los 4 Pasos (TODO)

### 1️⃣ Descargar
```python
import requests
respuesta = requests.get('https://ejemplo.com')
html = respuesta.text
```

### 2️⃣ Leer
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
```

### 3️⃣ Extraer
```python
elemento = soup.find('h2')
texto = elemento.text
```

### 4️⃣ Guardar
```python
import csv
with open('datos.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([texto])
```

---

## Los 5 Selectores (IMPORTANTE)

| Selector | Uso | Código |
|----------|-----|--------|
| Etiqueta | Encontrar el primero | `soup.find('h1')` |
| Todos | Encontrar todos | `soup.find_all('p')` |
| Clase | Por clase CSS | `soup.find('div', class_='contenido')` |
| ID | Por id | `soup.find('div', id='principal')` |
| Atributo | href, src, etc | `elemento['href']` |

---

## Código Simple (Copia esto)

```python
import requests
from bs4 import BeautifulSoup

# 1. Descargar
respuesta = requests.get('https://ejemplo.com')
html = respuesta.text

# 2. Leer
soup = BeautifulSoup(html, 'html.parser')

# 3. Extraer
for titulo in soup.find_all('h2'):
    print(titulo.text)

# 4. Guardar (ver archivo EJEMPLOS_COPIAR_PEGAR.md)
```

---

## ¿Cómo Ejecutar?

```bash
# 1. Instalar (una sola vez)
pip install requests beautifulsoup4

# 2. Ejecutar
python ejercicio19_simple.py
```

---

## Archivos Para Entender

| Archivo | Para Qué |
|---------|----------|
| `ejercicio19_simple.py` | **EJECUTA ESTO** - Ver ejemplos |
| `EXPLICACION_SIMPLE.md` | **LEE ESTO** - Entender paso a paso |
| `EJEMPLOS_COPIAR_PEGAR.md` | **USA ESTO** - Copiar código |
| `noticias_simples.csv` | Datos extraídos (ver resultado) |
| `productos_simples.json` | Datos extraídos (ver resultado) |

---

## Flujo Completo

```
┌─────────────┐
│ PAGINA WEB  │
└──────┬──────┘
       │ requests.get()
       ▼
┌─────────────┐
│    HTML     │ (texto)
└──────┬──────┘
       │ BeautifulSoup()
       ▼
┌─────────────────┐
│ OBJETO LEGIBLE  │ (soup)
└──────┬──────────┘
       │ soup.find()
       ▼
┌─────────────┐
│    DATOS    │
└──────┬──────┘
       │ csv.writer()
       ▼
┌─────────────┐
│ CSV o JSON  │
└─────────────┘
```

---

## Lo Más Fácil

```python
# 1. Importar
import requests
from bs4 import BeautifulSoup

# 2. Descargar
soup = BeautifulSoup(requests.get('url').text, 'html.parser')

# 3. Extraer
datos = [x.text for x in soup.find_all('h2')]

# 4. Imprimir
for dato in datos:
    print(dato)
```

---

## Recuerda

✅ **Hacer:**
- Usar `requests`
- Usar `BeautifulSoup`
- Guardar datos
- Probar código simple primero

❌ **NO hacer:**
- Sobrecargar servidores
- Ignorar si el sitio lo permite
- Copiar datos personales

---

## ¿Preguntas?

1. ¿Cómo extraigo precio? → Ver `EJEMPLOS_COPIAR_PEGAR.md` Ejemplo 4
2. ¿Cómo guardo en Excel? → Ver `EJEMPLOS_COPIAR_PEGAR.md` Ejemplo 5
3. ¿Qué hacer si falla? → Ver `EJEMPLOS_COPIAR_PEGAR.md` Ejemplo 7

---

## Próximo Paso

👉 Ejecuta: `python ejercicio19_simple.py`
👉 Luego abre los archivos `.csv` y `.json` generados
👉 Lee `EXPLICACION_SIMPLE.md` para entender

---

**¡Eso es web scraping! 🎉**
