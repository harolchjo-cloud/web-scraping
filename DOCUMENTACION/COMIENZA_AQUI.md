# ⭐ POR DÓNDE EMPEZAR - GUÍA PARA ESTUDIANTES

## 📋 Tu Ruta de Aprendizaje (45 minutos total)

### ⏰ Fase 1: Entiende (2 minutos)
```
Lee: RESUMEN_SIMPLE.md
```
Este archivo explica web scraping en 2 minutos.

### ⏰ Fase 2: Aprende (30 minutos)
```
Lee: EXPLICACION_SIMPLE.md
```
Aquí está TODO explicado paso a paso con ejemplos.

**Secciones:**
1. ¿Qué es Web Scraping?
2. Las 4 librerías que necesitas
3. Descargar una página
4. Leer HTML con BeautifulSoup
5. Los 5 selectores más usados
6. Ejemplo completo
7. Guardar en CSV
8. Guardar en JSON
9. Ejemplo REAL
10. Lo más importante (resumen)

### ⏰ Fase 3: Ve el Código (5 minutos)
```bash
python ejercicio19_simple.py
```

**Qué verás:**
- Explicación de selectores en acción
- Extracción de 3 noticias
- Extracción de 3 productos
- Archivos CSV generados
- Archivos JSON generados

### ⏰ Fase 4: Copia Ejemplos (5 minutos)
```
Lee: EJEMPLOS_COPIAR_PEGAR.md
```

10 ejemplos que puedes copiar y adaptar:
1. Extraer títulos
2. Extraer enlaces
3. Extraer de tablas
4. Extraer productos
5. Guardar en CSV
6. Guardar en JSON
7. Con manejo de errores
8. Limpiar espacios
9. Descargar varias páginas
10. Template base (copia esto)

### ⏰ Fase 5: Practica (5 minutos)
- Abre `noticias_simples.csv` (datos extraídos)
- Abre `noticias_simples.json` (datos en JSON)
- Mira cómo se ven los datos

---

## 📁 Archivos en la Carpeta

### Para Aprender
- ✅ `RESUMEN_SIMPLE.md` → Comienza aquí (2 min)
- ✅ `EXPLICACION_SIMPLE.md` → Lee después (30 min)
- ✅ `EJEMPLOS_COPIAR_PEGAR.md` → Copia código (15 min)

### Para Ejecutar
- ✅ `ejercicio19_simple.py` → Ejecuta esto

### Para Ver Resultados
- ✅ `noticias_simples.csv` → Abre con Notepad
- ✅ `noticias_simples.json` → Abre con Notepad
- ✅ `productos_simples.csv` → Abre con Notepad
- ✅ `productos_simples.json` → Abre con Notepad

---

## 🎯 Plan Paso a Paso (45 minutos)

```
0:00 - 0:02  ┃ Lee RESUMEN_SIMPLE.md
0:02 - 0:32  ┃ Lee EXPLICACION_SIMPLE.md
0:32 - 0:37  ┃ Ejecuta: python ejercicio19_simple.py
0:37 - 0:42  ┃ Lee EJEMPLOS_COPIAR_PEGAR.md
0:42 - 0:45  ┃ Abre y observa los archivos CSV y JSON
```

---

## 💻 Cómo Ejecutar el Código

### 1. Primero Instala (una sola vez)

```bash
pip install requests beautifulsoup4
```

**Nota:** Si ya lo hiciste antes, salta este paso.

### 2. Luego Ejecuta

```bash
python ejercicio19_simple.py
```

**Qué pasará:**
```
╔════════════════════════════╗
║ EJERCICIO 19 SIMPLE...     ║
╚════════════════════════════╝

SELECTORES CSS - LOS MÁS FÁCILES
============================================================

1. Buscar por ETIQUETA:
   Resultado: Título Principal

2. Buscar por CLASE:
   Resultado: <div class="contenido">...

... (más ejemplos)

EXTRAYENDO NOTICIAS
============================================================
Encontré 3 noticias

Título: Python es genial
Descripción: Python es fácil de aprender

(... más)

✓ ARCHIVO GUARDADO: noticias_simples.csv
✓ ARCHIVO GUARDADO: productos_simples.csv
```

### 3. Luego Abre los Archivos

**Para ver los datos en CSV:**
```bash
notepad noticias_simples.csv
```

**Para ver los datos en JSON:**
```bash
notepad noticias_simples.json
```

---

## 🔑 Lo CRÍTICO que debes entender

### Los 4 Pasos (SIEMPRE es esto)

```python
# 1. Descargar
import requests
html = requests.get('https://ejemplo.com').text

# 2. Leer
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 3. Extraer
elemento = soup.find('h2')  # O find_all()

# 4. Guardar
import csv
# (ver archivo EJEMPLOS_COPIAR_PEGAR.md Ejemplo 5)
```

### Los 5 Selectores (SIEMPRE UNO DE ESTOS)

```python
soup.find('h1')                    # 1. Por etiqueta
soup.find_all('p')                # 2. Todos
soup.find('div', class_='x')      # 3. Por clase
soup.find('div', id='x')          # 4. Por ID
elemento['href']                  # 5. Atributo
```

---

## ❓ Preguntas Frecuentes

### P1: ¿Por dónde empiezo?
**R:** Lee `RESUMEN_SIMPLE.md` (2 minutos)

### P2: No entiendo algo
**R:** Busca en `EXPLICACION_SIMPLE.md` (tiene TODO)

### P3: Quiero un ejemplo
**R:** Ve a `EJEMPLOS_COPIAR_PEGAR.md` (10 ejemplos)

### P4: Quiero copiar código
**R:** En `EJEMPLOS_COPIAR_PEGAR.md` hay template base

### P5: ¿Cómo ejecuto?
**R:** `python ejercicio19_simple.py`

### P6: El código me falla
**R:** Ver Ejemplo 7 en `EJEMPLOS_COPIAR_PEGAR.md` (manejo de errores)

### P7: ¿Dónde guardé los datos?
**R:** En los archivos `.csv` y `.json`

### P8: ¿Cómo abro CSV?
**R:** `notepad archivo.csv` o Excel

### P9: ¿Cómo abro JSON?
**R:** `notepad archivo.json` o editor de texto

### P10: ¿Qué hago después?
**R:** Sigue el orden: RESUMEN → EXPLICACION → EJEMPLOS → PRACTICA

---

## ✅ Checklist de Aprendizaje

- [ ] Leí RESUMEN_SIMPLE.md
- [ ] Leí EXPLICACION_SIMPLE.md
- [ ] Ejecuté python ejercicio19_simple.py
- [ ] Abrí los archivos CSV generados
- [ ] Abrí los archivos JSON generados
- [ ] Leí EJEMPLOS_COPIAR_PEGAR.md
- [ ] Copié un ejemplo y lo adapté
- [ ] Entiendo los 4 pasos
- [ ] Entiendo los 5 selectores
- [ ] Puedo ejecutar código básico

**Si marcaste TODO ✓ = ¡Ya sabes web scraping!**

---

## 🎉 ¡Felicidades!

Después de estos 45 minutos:

✅ Entiendes qué es web scraping  
✅ Sabes las 4 librerías principales  
✅ Conoces los 5 selectores  
✅ Puedes extraer datos  
✅ Puedes guardar en CSV/JSON  
✅ Puedes ejecutar código

---

## 📚 Próximos Pasos (OPCIONAL)

Después de dominar lo básico:

1. **Extrae de un sitio REAL** (respetando reglas)
2. **Aprende Selenium** (para sitios con JavaScript)
3. **Usa pandas** para análisis
4. **Automatiza** con cron/scheduler

---

**¡Comienza AHORA! 🚀**

👉 Primer paso: **Lee `RESUMEN_SIMPLE.md`** (2 minutos)
