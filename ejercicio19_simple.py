"""
EJERCICIO 19 SIMPLE: Web Scraping para Principiantes
Extracción de datos web - Versión fácil de entender
"""

# ============================================================================
# PASO 1: IMPORTAR LAS LIBRERÍAS QUE NECESITAMOS
# ============================================================================

import requests                    # Para descargar páginas web
from bs4 import BeautifulSoup     # Para leer el HTML
import csv                         # Para guardar datos en Excel-like
import json                        # Para guardar datos en formato JSON


# ============================================================================
# PASO 2: CREAR UNA FUNCIÓN SIMPLE PARA DESCARGAR UNA PÁGINA
# ============================================================================

def descargar_pagina(url):
    """
    Descarga una página web y la devuelve como texto
    
    Parámetros:
        url (str): La dirección del sitio web
    
    Devuelve:
        str: El código HTML de la página
    """
    # Primero decimos quiénes somos (algunos sitios lo piden)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    try:
        # Descargar la página
        respuesta = requests.get(url, headers=headers, timeout=5)
        print(f"✓ Página descargada: {url}")
        return respuesta.text  # Devolver el HTML
    except Exception as e:
        print(f"✗ Error al descargar: {e}")
        return None


# ============================================================================
# PASO 3: FUNCIÓN PARA LEER Y PARSEAR HTML
# ============================================================================

def parsear_html(html_texto):
    """
    Lee el HTML y lo convierte en algo que podamos leer fácilmente
    
    Parámetros:
        html_texto (str): El código HTML como texto
    
    Devuelve:
        BeautifulSoup: Objeto que podemos consultar
    """
    soup = BeautifulSoup(html_texto, 'html.parser')
    return soup


# ============================================================================
# PASO 4: EJEMPLOS SIMPLES DE EXTRACCIÓN
# ============================================================================

# Ejemplo 1: HTML de prueba con noticias
html_noticias = """
<html>
    <body>
        <div class="noticia">
            <h2>Python es genial</h2>
            <p>Python es fácil de aprender</p>
        </div>
        
        <div class="noticia">
            <h2>Web Scraping fácil</h2>
            <p>Extraer datos es simple</p>
        </div>
        
        <div class="noticia">
            <h2>BeautifulSoup mola</h2>
            <p>Parsear HTML es fácil</p>
        </div>
    </body>
</html>
"""


def extraer_noticias_simple():
    """
    Extrae noticias del HTML de ejemplo
    """
    print("\n" + "="*60)
    print("EXTRAYENDO NOTICIAS")
    print("="*60)
    
    # 1. Parsear el HTML
    soup = parsear_html(html_noticias)
    
    # 2. Buscar todos los elementos con clase "noticia"
    noticias = soup.find_all('div', class_='noticia')
    
    print(f"Encontré {len(noticias)} noticias\n")
    
    # 3. Para cada noticia, extraer el título
    datos = []
    for noticia in noticias:
        # Encontrar el h2 dentro de esta noticia
        titulo = noticia.find('h2').text
        # Encontrar el párrafo dentro de esta noticia
        descripcion = noticia.find('p').text
        
        print(f"Título: {titulo}")
        print(f"Descripción: {descripcion}")
        print()
        
        # Guardar en una lista
        datos.append({
            'titulo': titulo,
            'descripcion': descripcion
        })
    
    return datos


# ============================================================================
# PASO 5: EJEMPLO 2 - PRODUCTOS CON PRECIOS
# ============================================================================

html_productos = """
<html>
    <body>
        <div class="producto">
            <h3>Laptop</h3>
            <span class="precio">$500</span>
        </div>
        
        <div class="producto">
            <h3>Mouse</h3>
            <span class="precio">$20</span>
        </div>
        
        <div class="producto">
            <h3>Teclado</h3>
            <span class="precio">$80</span>
        </div>
    </body>
</html>
"""


def extraer_productos_simple():
    """
    Extrae productos y precios
    """
    print("\n" + "="*60)
    print("EXTRAYENDO PRODUCTOS")
    print("="*60)
    
    soup = parsear_html(html_productos)
    productos = soup.find_all('div', class_='producto')
    
    print(f"Encontré {len(productos)} productos\n")
    
    datos = []
    for producto in productos:
        # Extraer nombre
        nombre = producto.find('h3').text
        
        # Extraer precio (viene con $, lo quitamos)
        precio_texto = producto.find('span', class_='precio').text
        precio = float(precio_texto.replace('$', ''))
        
        print(f"Producto: {nombre}")
        print(f"Precio: ${precio}")
        print()
        
        datos.append({
            'nombre': nombre,
            'precio': precio
        })
    
    return datos


# ============================================================================
# PASO 6: GUARDAR DATOS EN CSV
# ============================================================================

def guardar_en_csv(datos, nombre_archivo):
    """
    Guarda datos en un archivo CSV (como Excel)
    
    Parámetros:
        datos (list): Lista de diccionarios
        nombre_archivo (str): Nombre del archivo CSV
    """
    if not datos:
        print("No hay datos para guardar")
        return
    
    # Abrir archivo para escribir
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        # Obtener los nombres de columnas (claves del diccionario)
        columnas = datos[0].keys()
        
        # Crear el escritor CSV
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        
        # Escribir encabezados
        escritor.writeheader()
        
        # Escribir cada fila
        escritor.writerows(datos)
    
    print(f"✓ Archivo guardado: {nombre_archivo}")


# ============================================================================
# PASO 7: GUARDAR DATOS EN JSON
# ============================================================================

def guardar_en_json(datos, nombre_archivo):
    """
    Guarda datos en un archivo JSON
    
    Parámetros:
        datos (list): Lista de diccionarios
        nombre_archivo (str): Nombre del archivo JSON
    """
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)
    
    print(f"✓ Archivo guardado: {nombre_archivo}")


# ============================================================================
# PASO 8: BUSCAR ELEMENTOS - LOS SELECTORES MÁS USADOS
# ============================================================================

def ejemplos_selectores():
    """
    Muestra los selectores CSS más comunes y fáciles
    """
    print("\n" + "="*60)
    print("SELECTORES CSS - LOS MÁS FÁCILES")
    print("="*60)
    
    html = """
    <html>
        <body>
            <h1>Título Principal</h1>
            <div class="contenido">
                <p>Texto en un párrafo</p>
                <a href="https://ejemplo.com">Enlace</a>
            </div>
            <div id="especial">
                Contenido especial
            </div>
        </body>
    </html>
    """
    
    soup = parsear_html(html)
    
    print("\n1. Buscar por ETIQUETA:")
    print("   soup.find('h1')")
    h1 = soup.find('h1')
    print(f"   Resultado: {h1.text}\n")
    
    print("2. Buscar por CLASE:")
    print("   soup.find('div', class_='contenido')")
    div = soup.find('div', class_='contenido')
    print(f"   Resultado: {div}\n")
    
    print("3. Buscar por ID:")
    print("   soup.find('div', id='especial')")
    especial = soup.find('div', id='especial')
    print(f"   Resultado: {especial.text}\n")
    
    print("4. Buscar TODOS los de un tipo:")
    print("   soup.find_all('p')")
    parrafos = soup.find_all('p')
    print(f"   Resultado: {len(parrafos)} párrafo(s)\n")
    
    print("5. Obtener ATRIBUTO:")
    print("   enlace.get('href')")
    enlace = soup.find('a')
    print(f"   Resultado: {enlace.get('href')}\n")


# ============================================================================
# PASO 9: FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal - ejecuta todo
    """
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  EJERCICIO 19 SIMPLE: WEB SCRAPING PARA PRINCIPIANTES".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "="*58 + "╝")
    
    # Ejecutar ejemplos de selectores
    ejemplos_selectores()
    
    # Ejemplo 1: Extraer noticias
    noticias = extraer_noticias_simple()
    guardar_en_csv(noticias, 'noticias_simples.csv')
    guardar_en_json(noticias, 'noticias_simples.json')
    
    # Ejemplo 2: Extraer productos
    productos = extraer_productos_simple()
    guardar_en_csv(productos, 'productos_simples.csv')
    guardar_en_json(productos, 'productos_simples.json')
    
    # Mostrar resumen
    print("\n" + "="*60)
    print("✓ EJERCICIO COMPLETADO")
    print("="*60)
    print(f"\nArchivos generados:")
    print(f"  • noticias_simples.csv")
    print(f"  • noticias_simples.json")
    print(f"  • productos_simples.csv")
    print(f"  • productos_simples.json")
    print("\n¡Abre estos archivos para ver los datos extraídos!\n")


# ============================================================================
# EJECUTAR
# ============================================================================

if __name__ == "__main__":
    main()
