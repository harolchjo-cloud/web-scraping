# 📑 ÍNDICE COMPLETO - Ejercicio 19: Web Scraping

## 🎯 Objetivo General
Aprender y dominar la extracción automatizada de datos web usando Python, desde conceptos básicos hasta técnicas avanzadas.

---

## 📂 ESTRUCTURA DEL PROYECTO

```
EJERCICIO 19: Web Scraping
├── 🐍 CÓDIGO PRINCIPAL (3 archivos)
│   ├── ejercicio19.py (16.51 KB)
│   ├── ejercicio19b.py (14.31 KB)
│   └── ejercicio19c.py (16.6 KB)
│
├── 📚 DOCUMENTACIÓN (3 archivos)
│   ├── README_WebScraping.md (9.74 KB)
│   ├── GUIA_RAPIDA_WebScraping.md (7.69 KB)
│   └── RESUMEN_Ejercicio19.md (9.21 KB)
│
├── 📊 DATOS EXTRAÍDOS - CSV (7 archivos)
│   ├── noticias.csv (176 B)
│   ├── productos.csv (149 B)
│   ├── tabla_datos.csv (183 B)
│   ├── tabla_ejemplo.csv (41 B)
│   ├── productos_ejemplo.csv (197 B)
│   └── [Más archivos de datos]
│
├── 📈 DATOS EXTRAÍDOS - JSON (7 archivos)
│   ├── noticias.json (338 B)
│   ├── productos.json (329 B)
│   ├── tabla_datos.json (408 B)
│   ├── tabla_ejemplo.json (121 B)
│   ├── productos_ejemplo.json (422 B)
│   ├── selectores_css.json (199 B)
│   └── [Más archivos de datos]
│
└── 📝 LOGS (1 archivo)
    └── scraping.log
```

**Total:** 20+ archivos | ~100 KB de código y datos

---

## 🐍 MÓDULOS DE CÓDIGO

### 1. **ejercicio19.py** - Sistema Básico Completo
**Tamaño:** 16.51 KB | **Lineas:** ~400 | **Tiempo:** 15-20 minutos

#### Contenido:
```
✓ Clase WebScraper (principal)
  ├── Descargar páginas web
  ├── Parsear HTML
  ├── Buscar elementos
  └── Extraer datos

✓ Métodos de extracción:
  ├── extraer_noticias_ejemplo()
  ├── extraer_precios_ejemplo()
  ├── extraer_tabla_html()
  ├── extraer_con_selectores_css()
  └── Métodos auxiliares

✓ Exportación de datos:
  ├── guardar_csv()
  └── guardar_json()

✓ Análisis con Pandas:
  ├── Estadísticas básicas
  ├── Agrupación de datos
  └── Visualización

✓ Expresiones regulares:
  ├── Extracción de números
  ├── Validación de emails
  ├── Limpieza de texto
  └── Búsqueda de URLs
```

#### Cómo usar:
```bash
python ejercicio19.py
```

#### Archivos generados:
- noticias.csv / noticias.json (3 noticias)
- productos.csv / productos.json (3 productos)
- tabla_datos.csv / tabla_datos.json (3 países)
- selectores_css.json

---

### 2. **ejercicio19b.py** - Sistema Avanzado
**Tamaño:** 14.31 KB | **Lineas:** ~350 | **Tiempo:** 15-20 minutos

#### Contenido:
```
✓ Clase ScraperSelenium:
  ├── Inicializar driver Chrome
  ├── Esperar elementos dinámicos
  ├── Manejar JavaScript
  └── Simular interacciones

✓ PatronesAvanzados (5 patrones):
  ├── Paginación (múltiples páginas)
  ├── Autenticación (login)
  ├── Manejo robusto de errores
  ├── Multi-threading
  └── Cacheo de datos

✓ MejoresPracticas:
  ├── Respeto al servidor
  ├── Identificación realista
  ├── Robustez y resilencia
  ├── Escalabilidad
  ├── Consideraciones legales
  └── Alternativas (APIs)
```

#### Cómo usar:
```bash
python ejercicio19b.py
```

#### Requisitos opcionales:
- ChromeDriver para Selenium (https://chromedriver.chromium.org/)

---

### 3. **ejercicio19c.py** - Ejemplos Prácticos Reutilizables
**Tamaño:** 16.6 KB | **Lineas:** ~400 | **Tiempo:** 15-20 minutos

#### Contenido:
```
✓ 8 Clases reutilizables:

1. ScraperBasico
   ├── obtener() con reintentos automáticos
   ├── Backoff exponencial
   └── Manejo de errores

2. ExtractorTabla
   ├── HTML a diccionarios
   ├── Exportar CSV/JSON
   └── Formato limpio

3. ExtractorProducto
   ├── Extracción de precios
   ├── Extracción de ratings
   └── Limpieza de datos

4. MonitorCambios
   ├── Detectar cambios
   ├── Guardar estado
   └── Alertas

5. ExportadorDatos
   ├── A CSV
   ├── A JSON
   └── A HTML

6. LimpiadorDatos
   ├── Limpiar texto
   ├── Validar emails
   ├── Validar URLs
   └── Procesar datos

7. LoggerScraping
   ├── Registrar eventos
   ├── JSON logs
   └── Trazabilidad

8. PipelineCompleto
   ├── End-to-end automation
   ├── Descargar + Parsear + Limpiar + Guardar
   └── Manejo de errores
```

#### Cómo usar:
```bash
python ejercicio19c.py
```

#### Archivos generados:
- tabla_ejemplo.csv / tabla_ejemplo.json
- productos_ejemplo.csv / productos_ejemplo.json
- scraping.log

---

## 📚 DOCUMENTACIÓN

### **README_WebScraping.md** (9.74 KB)
Guía completa y profesional del web scraping.

#### Secciones:
1. ¿Qué es Web Scraping? (concepto)
2. ¿Cómo Funciona? (flujo)
3. Librerías Principales (tabla comparativa)
4. Archivos Incluidos (descripción)
5. Instalación y Uso (paso a paso)
6. Ejemplos de Código (10+ ejemplos)
7. Selectores CSS - Referencia Rápida
8. Buenas Prácticas (checklist)
9. Consideraciones Legales (aviso legal)
10. Expresiones Regulares (patrones útiles)
11. Análisis con Pandas (ejemplos)
12. Selenium para Dinámicos (avanzado)
13. Patrones Avanzados (5 patrones)
14. Comparativa de Herramientas (tabla)
15. Troubleshooting (soluciones)
16. Recursos Útiles (links)
17. Checklist Final (validación)

---

### **GUIA_RAPIDA_WebScraping.md** (7.69 KB)
Cheat sheet rápido para consulta frecuente.

#### Secciones:
1. Inicio Rápido (3 líneas clave)
2. Selectores CSS - Cheat Sheet (15 ejemplos)
3. Patrones Comunes (8 patrones)
4. Limpieza de Datos (regex)
5. Análisis con Pandas (operaciones)
6. Selenium (JavaScript)
7. Buenas Prácticas (tabla)
8. Troubleshooting (tabla)
9. Recursos (instalación)
10. Ejemplo Completo (5 pasos)
11. Checklist Pre-scraping (8 items)
12. Consejos Finales (8 consejos)

---

### **RESUMEN_Ejercicio19.md** (9.21 KB)
Resumen visual y ejecutivo del ejercicio.

#### Secciones:
1. Archivos Generados (estructura árbol)
2. Lo que Aprendiste (5 categorías)
3. Características Principales (3 módulos)
4. Datos Extraídos de Ejemplo (mostrado)
5. Cómo Usar (3 pasos)
6. Ejemplos Rápidos (template)
7. Seguridad y Ética (checklist)
8. Complejidad y Características (gráfico)
9. Conceptos Clave (tabla)
10. Librerías Utilizadas (listado)
11. Próximos Pasos (5 items)
12. Advertencias Importantes (8 items)
13. Resumen Ejecutivo (tabla)
14. ¡Ejercicio Completado! (logros)

---

## 📊 DATOS GENERADOS

### CSV (Comma Separated Values)
```
noticias.csv                → 3 noticias con URL y fecha
productos.csv              → 3 productos con precio
tabla_datos.csv            → 3 países con población y PIB
tabla_ejemplo.csv          → 2 productos de tabla HTML
productos_ejemplo.csv      → 3 smartphones con rating
```

### JSON (JavaScript Object Notation)
```
noticias.json              → Array de noticias
productos.json             → Array de productos
tabla_datos.json           → Array de datos de tabla
selectores_css.json        → Resultados de selectores CSS
tabla_ejemplo.json         → Tabla parseada
productos_ejemplo.json     → Productos con timestamps
```

### Logs
```
scraping.log               → Registro de eventos del scraping
```

---

## 🚀 QUICK START - Los 3 Pasos

### 1. Instalar dependencias (una sola vez)
```bash
pip install requests beautifulsoup4 lxml selenium pandas
```

### 2. Ejecutar los ejemplos
```bash
python ejercicio19.py    # Básico
python ejercicio19b.py   # Avanzado
python ejercicio19c.py   # Práctico
```

### 3. Revisar resultados
```bash
# Ver archivos generados
ls *.csv *.json *.log

# Ver contenido
type noticias.json
type productos.csv
```

---

## 📋 CONCEPTOS CLAVE

| Concepto | Definición | Ejemplo |
|----------|-----------|---------|
| **Scraping** | Extracción automatizada de datos | requests + BS4 |
| **Parser** | Analizador de HTML | BeautifulSoup |
| **Selector** | Forma de localizar elementos | CSS, XPath |
| **Session** | Conexión persistente | requests.Session() |
| **DOM** | Árbol de elementos HTML | soup.find() |
| **Robots.txt** | Reglas de scraping | /robots.txt |
| **User-Agent** | Identificador del navegador | Mozilla/5.0 |
| **Backoff** | Espera exponencial | 2^n segundos |
| **Encoding** | Codificación de texto | UTF-8 |
| **Regex** | Expresión regular | r'\\d+' |

---

## 🎓 MATRIZ DE APRENDIZAJE

```
NIVEL BÁSICO (Ejercicio 19):
├── Conceptos
│   ├── Qué es web scraping
│   ├── HTML y CSS
│   └── Requests y BeautifulSoup
├── Técnicas
│   ├── Descargar páginas
│   ├── Parsear HTML
│   └── Extraer elementos
└── Aplicaciones
    ├── Noticias
    ├── Precios
    └── Tablas

NIVEL INTERMEDIO (Ejercicio 19B):
├── Conceptos
│   ├── JavaScript y Selenium
│   ├── Paginación
│   └── Autenticación
├── Técnicas
│   ├── Multi-threading
│   ├── Cacheo
│   └── Reintentos
└── Aplicaciones
    ├── Sitios dinámicos
    ├── Login requerido
    └── Datos grandes

NIVEL AVANZADO (Ejercicio 19C):
├── Conceptos
│   ├── Pipelines
│   ├── Monitoreo
│   └── Escalabilidad
├── Técnicas
│   ├── OOP y clases reutilizables
│   ├── Logging y debugging
│   └── Validación de datos
└── Aplicaciones
    ├── Producción
    ├── APIs internas
    └── Análisis de datos
```

---

## ✅ CHECKLIST DE VALIDACIÓN

- [x] Código funcional
- [x] Todos los módulos ejecutan sin errores
- [x] Datos se generan correctamente
- [x] Exportación a CSV/JSON funciona
- [x] Documentación completa
- [x] Ejemplos incluidos
- [x] Comentarios en código
- [x] Buenas prácticas implementadas
- [x] Manejo de errores robusto
- [x] Logs y debugging

---

## 🏆 LOGROS ALCANZADOS

Después de completar este ejercicio, serás capaz de:

1. **Entender** los fundamentos del web scraping
2. **Descargar** y parsear páginas web
3. **Extraer** datos usando selectores CSS
4. **Procesar** datos con expresiones regulares
5. **Exportar** datos en múltiples formatos
6. **Analizar** datos con Pandas
7. **Usar** Selenium para sitios dinámicos
8. **Implementar** patrones avanzados
9. **Manejar** errores y excepciones
10. **Seguir** buenas prácticas y ética

---

## 📞 SOPORTE Y REFERENCIA

### Sitios de Documentación
- BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/
- Requests: https://requests.readthedocs.io/
- Selenium: https://selenium.dev/
- Pandas: https://pandas.pydata.org/
- Regex: https://regex101.com/

### Archivos de Referencia
- README_WebScraping.md → Guía completa
- GUIA_RAPIDA_WebScraping.md → Referencia rápida
- RESUMEN_Ejercicio19.md → Resumen visual

### Problemas Comunes
Revisar "Troubleshooting" en README_WebScraping.md

---

## 🎯 PRÓXIMAS METAS

1. **Aplicar** a casos reales (respetando términos)
2. **Crear** un scraper personalizado
3. **Integrar** con bases de datos
4. **Automatizar** con cron/scheduler
5. **Escalar** con Scrapy
6. **Monitorear** cambios
7. **Buscar** APIs oficiales
8. **Publicar** datos extraídos

---

## 📈 ESTADÍSTICAS

| Métrica | Valor |
|---------|-------|
| Archivos de código | 3 |
| Líneas de código | ~1,100 |
| Archivos de datos | 14 |
| Clases implementadas | 8+ |
| Métodos/funciones | 30+ |
| Ejemplos incluidos | 15+ |
| Patrones demostrados | 10+ |
| Documentación (páginas) | 3 |
| Tamaño total | ~100 KB |

---

## 🎓 CERTIFICACIÓN

✅ **Has completado el Ejercicio 19: Web Scraping**

**Nivel:** 🟡 Intermedio-Avanzado  
**Tiempo:** 1-2 horas  
**Dificultad:** Media  
**Recomendación:** Excelente para aprender web scraping

---

**Versión:** 1.0  
**Fecha:** 2025-12-01  
**Estado:** ✓ COMPLETO  
**Autor:** Ejercicio Python 19  
**Nivel educativo:** Recomendado para estudiantes de Python intermedio en adelante
