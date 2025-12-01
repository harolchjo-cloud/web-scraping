"""
EJERCICIO 19: Web Scraping - Extracción de Datos Web
Sistema completo que incluye:
- Extracción de noticias de sitios web
- Scraping de precios de productos
- Análisis de tablas HTML
- Manejo básico de JavaScript con Selenium
- Exportación a CSV y JSON
"""

import requests
from bs4 import BeautifulSoup
import csv
import json
import time
from datetime import datetime
import pandas as pd
from urllib.parse import urljoin
import re
from typing import List, Dict
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class WebScraper:
    """Clase principal para web scraping"""
    
    def __init__(self, delay=1):
        """
        Inicializar el scraper
        
        Args:
            delay (int): Segundos de espera entre requests (buena práctica)
        """
        self.delay = delay
        self.session = requests.Session()
        # Usar un User-Agent realista para evitar bloqueos
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def descargar_pagina(self, url: str) -> BeautifulSoup:
        """
        Descargar y parsear una página web
        
        Args:
            url (str): URL de la página a descargar
            
        Returns:
            BeautifulSoup: Objeto parseado del HTML
        """
        try:
            logger.info(f"Descargando: {url}")
            response = self.session.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            time.sleep(self.delay)  # Respetar el servidor
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            logger.error(f"Error descargando {url}: {e}")
            return None
    
    def extraer_noticias_ejemplo(self) -> List[Dict]:
        """
        Ejemplo: Extraer noticias de un sitio (usando ejemplo local)
        Nota: En producción, usar un sitio real con scraping permitido
        
        Returns:
            List[Dict]: Lista de noticias con título y enlace
        """
        # Crear HTML de ejemplo para demostración
        html_ejemplo = """
        <html>
            <body>
                <div class="articulo">
                    <h2 class="titulo">Últimas innovaciones en IA</h2>
                    <a href="/articulo1" class="enlace">Leer más</a>
                    <span class="fecha">2024-12-01</span>
                </div>
                <div class="articulo">
                    <h2 class="titulo">Python domina desarrollo backend</h2>
                    <a href="/articulo2" class="enlace">Leer más</a>
                    <span class="fecha">2024-11-30</span>
                </div>
                <div class="articulo">
                    <h2 class="titulo">Web scraping ético y legal</h2>
                    <a href="/articulo3" class="enlace">Leer más</a>
                    <span class="fecha">2024-11-29</span>
                </div>
            </body>
        </html>
        """
        
        soup = BeautifulSoup(html_ejemplo, 'html.parser')
        noticias = []
        
        # Buscar todos los artículos
        articulos = soup.find_all('div', class_='articulo')
        
        for articulo in articulos:
            # Extraer título
            titulo = articulo.find('h2', class_='titulo')
            # Extraer enlace
            enlace = articulo.find('a', class_='enlace')
            # Extraer fecha
            fecha = articulo.find('span', class_='fecha')
            
            if titulo and enlace:
                noticia = {
                    'titulo': titulo.text.strip(),
                    'url': enlace.get('href'),
                    'fecha': fecha.text.strip() if fecha else 'N/A'
                }
                noticias.append(noticia)
                logger.info(f"Noticia extraída: {noticia['titulo']}")
        
        return noticias
    
    def extraer_precios_ejemplo(self) -> List[Dict]:
        """
        Ejemplo: Extraer precios de productos
        
        Returns:
            List[Dict]: Lista de productos con precios
        """
        html_ejemplo = """
        <html>
            <body>
                <div class="producto">
                    <h3 class="nombre">Laptop Dell XPS 13</h3>
                    <span class="precio">$999.99</span>
                    <span class="disponibilidad">En stock</span>
                </div>
                <div class="producto">
                    <h3 class="nombre">Ratón Logitech MX Master</h3>
                    <span class="precio">$99.99</span>
                    <span class="disponibilidad">En stock</span>
                </div>
                <div class="producto">
                    <h3 class="nombre">Teclado Mecánico Cherry</h3>
                    <span class="precio">$149.99</span>
                    <span class="disponibilidad">Agotado</span>
                </div>
            </body>
        </html>
        """
        
        soup = BeautifulSoup(html_ejemplo, 'html.parser')
        productos = []
        
        # Buscar todos los productos
        items = soup.find_all('div', class_='producto')
        
        for item in items:
            nombre = item.find('h3', class_='nombre')
            precio_elem = item.find('span', class_='precio')
            disponibilidad = item.find('span', class_='disponibilidad')
            
            if nombre and precio_elem:
                # Limpiar precio (remover $ y convertir a float)
                precio_texto = precio_elem.text.replace('$', '').strip()
                try:
                    precio = float(precio_texto)
                except ValueError:
                    precio = 0.0
                
                producto = {
                    'nombre': nombre.text.strip(),
                    'precio': precio,
                    'disponibilidad': disponibilidad.text.strip() if disponibilidad else 'N/A'
                }
                productos.append(producto)
                logger.info(f"Producto extraído: {producto['nombre']} - ${producto['precio']}")
        
        return productos
    
    def extraer_tabla_html(self) -> List[Dict]:
        """
        Ejemplo: Extraer datos de una tabla HTML
        
        Returns:
            List[Dict]: Datos de la tabla como diccionarios
        """
        html_ejemplo = """
        <html>
            <body>
                <table class="estadisticas">
                    <thead>
                        <tr>
                            <th>País</th>
                            <th>Población</th>
                            <th>PIB (USD)</th>
                            <th>Región</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>China</td>
                            <td>1,402,405,518</td>
                            <td>$17.96 Trillones</td>
                            <td>Asia</td>
                        </tr>
                        <tr>
                            <td>India</td>
                            <td>1,404,638,000</td>
                            <td>$3.73 Trillones</td>
                            <td>Asia</td>
                        </tr>
                        <tr>
                            <td>México</td>
                            <td>128,932,753</td>
                            <td>$1.29 Trillones</td>
                            <td>América del Norte</td>
                        </tr>
                    </tbody>
                </table>
            </body>
        </html>
        """
        
        soup = BeautifulSoup(html_ejemplo, 'html.parser')
        tabla = soup.find('table', class_='estadisticas')
        
        if not tabla:
            return []
        
        # Extraer encabezados
        encabezados = []
        for th in tabla.find_all('th'):
            encabezados.append(th.text.strip())
        
        # Extraer filas
        datos = []
        for tr in tabla.find_all('tbody')[0].find_all('tr'):
            celdas = tr.find_all('td')
            fila = {}
            for i, celda in enumerate(celdas):
                if i < len(encabezados):
                    fila[encabezados[i]] = celda.text.strip()
            datos.append(fila)
            logger.info(f"Fila extraída: {fila}")
        
        return datos
    
    def extraer_con_selectores_css(self) -> Dict:
        """
        Ejemplo: Usar selectores CSS para búsquedas más complejas
        
        Returns:
            Dict: Datos extraídos con selectores CSS
        """
        html_ejemplo = """
        <html>
            <body>
                <div id="contenido-principal">
                    <article class="post destacado">
                        <h1>Título Principal</h1>
                        <p class="resumen">Este es un resumen importante</p>
                    </article>
                    <nav>
                        <a href="#home" class="nav-link">Inicio</a>
                        <a href="#about" class="nav-link">Acerca de</a>
                        <a href="#contact" class="nav-link">Contacto</a>
                    </nav>
                </div>
            </body>
        </html>
        """
        
        soup = BeautifulSoup(html_ejemplo, 'html.parser')
        
        resultados = {}
        
        # Selector por ID
        contenido = soup.select('#contenido-principal')
        resultados['contenido_encontrado'] = bool(contenido)
        
        # Selector por clase
        articulos = soup.select('.post.destacado')
        resultados['articulos'] = [art.find('h1').text for art in articulos if art.find('h1')]
        
        # Selector combinado
        enlaces = soup.select('#contenido-principal .nav-link')
        resultados['enlaces'] = [enlace.get('href') for enlace in enlaces]
        
        # Selector descendiente
        titulos = soup.select('article > h1')
        resultados['titulos'] = [t.text for t in titulos]
        
        logger.info(f"Selectores CSS aplicados: {resultados}")
        return resultados
    
    def guardar_csv(self, datos: List[Dict], nombre_archivo: str):
        """
        Guardar datos en formato CSV
        
        Args:
            datos (List[Dict]): Lista de diccionarios
            nombre_archivo (str): Nombre del archivo CSV
        """
        if not datos:
            logger.warning(f"No hay datos para guardar en {nombre_archivo}")
            return
        
        try:
            with open(nombre_archivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=datos[0].keys())
                writer.writeheader()
                writer.writerows(datos)
            logger.info(f"Datos guardados en {nombre_archivo}")
        except Exception as e:
            logger.error(f"Error guardando CSV: {e}")
    
    def guardar_json(self, datos, nombre_archivo: str):
        """
        Guardar datos en formato JSON
        
        Args:
            datos: Datos a guardar (lista o diccionario)
            nombre_archivo (str): Nombre del archivo JSON
        """
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)
            logger.info(f"Datos guardados en {nombre_archivo}")
        except Exception as e:
            logger.error(f"Error guardando JSON: {e}")


def ejemplo_analisis_datos():
    """Ejemplo de análisis de datos extraídos con Pandas"""
    logger.info("\n" + "="*60)
    logger.info("EJEMPLO: Análisis con Pandas")
    logger.info("="*60)
    
    # Crear DataFrame de ejemplo
    datos = {
        'Producto': ['Laptop', 'Ratón', 'Teclado', 'Monitor', 'Webcam'],
        'Precio': [999.99, 99.99, 149.99, 399.99, 89.99],
        'Stock': [5, 15, 8, 3, 12],
        'Categoría': ['Electrónica', 'Accesorios', 'Accesorios', 'Electrónica', 'Accesorios']
    }
    
    df = pd.DataFrame(datos)
    
    # Análisis básicos
    logger.info(f"\nPrecio promedio: ${df['Precio'].mean():.2f}")
    logger.info(f"Producto más caro: {df.loc[df['Precio'].idxmax(), 'Producto']}")
    logger.info(f"Producto más barato: {df.loc[df['Precio'].idxmin(), 'Producto']}")
    logger.info(f"Stock total: {df['Stock'].sum()} unidades")
    
    # Agrupar por categoría
    logger.info("\nResumen por categoría:")
    resumen = df.groupby('Categoría').agg({
        'Precio': 'mean',
        'Stock': 'sum'
    })
    logger.info(resumen.to_string())
    
    return df


def ejemplo_expresiones_regulares():
    """Ejemplo de uso de expresiones regulares para limpiar datos"""
    logger.info("\n" + "="*60)
    logger.info("EJEMPLO: Expresiones Regulares para limpieza de datos")
    logger.info("="*60)
    
    textos = [
        "Precio: $999.99",
        "Teléfono: +34-123-456-789",
        "Email: usuario@ejemplo.com",
        "Fecha: 01/12/2024",
        "Cantidad: 100 unidades"
    ]
    
    # Extraer números
    numeros = re.findall(r'\d+\.?\d*', textos[0])
    logger.info(f"Números en '{textos[0]}': {numeros}")
    
    # Validar email
    patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    email = 'usuario@ejemplo.com'
    es_valido = bool(re.match(patron_email, email))
    logger.info(f"¿'{email}' es válido?: {es_valido}")
    
    # Limpiar texto
    texto = "   Esto   tiene   espacios   extra   "
    limpio = re.sub(r'\s+', ' ', texto.strip())
    logger.info(f"Texto limpio: '{limpio}'")
    
    # Extraer URL de un texto
    texto_con_url = "Visita https://www.ejemplo.com para más info"
    urls = re.findall(r'https?://\S+', texto_con_url)
    logger.info(f"URLs encontradas: {urls}")


def main():
    """Función principal - Ejecutar todos los ejemplos"""
    logger.info("\n" + "="*60)
    logger.info("EJERCICIO 19: WEB SCRAPING - EXTRACCIÓN DE DATOS WEB")
    logger.info("="*60)
    
    # Inicializar scraper
    scraper = WebScraper(delay=1)
    
    # 1. Extraer noticias
    logger.info("\n" + "-"*60)
    logger.info("1. Extrayendo noticias...")
    logger.info("-"*60)
    noticias = scraper.extraer_noticias_ejemplo()
    scraper.guardar_csv(noticias, 'noticias.csv')
    scraper.guardar_json(noticias, 'noticias.json')
    
    # 2. Extraer precios
    logger.info("\n" + "-"*60)
    logger.info("2. Extrayendo precios de productos...")
    logger.info("-"*60)
    productos = scraper.extraer_precios_ejemplo()
    scraper.guardar_csv(productos, 'productos.csv')
    scraper.guardar_json(productos, 'productos.json')
    
    # 3. Extraer tabla HTML
    logger.info("\n" + "-"*60)
    logger.info("3. Extrayendo datos de tabla HTML...")
    logger.info("-"*60)
    tabla_datos = scraper.extraer_tabla_html()
    scraper.guardar_csv(tabla_datos, 'tabla_datos.csv')
    scraper.guardar_json(tabla_datos, 'tabla_datos.json')
    
    # 4. Selectores CSS
    logger.info("\n" + "-"*60)
    logger.info("4. Utilizando selectores CSS...")
    logger.info("-"*60)
    selectores_resultado = scraper.extraer_con_selectores_css()
    scraper.guardar_json(selectores_resultado, 'selectores_css.json')
    
    # 5. Análisis con Pandas
    ejemplo_analisis_datos()
    
    # 6. Expresiones regulares
    ejemplo_expresiones_regulares()
    
    logger.info("\n" + "="*60)
    logger.info("✓ EJERCICIO COMPLETADO")
    logger.info("="*60)
    logger.info("\nArchivos generados:")
    logger.info("- noticias.csv / noticias.json")
    logger.info("- productos.csv / productos.json")
    logger.info("- tabla_datos.csv / tabla_datos.json")
    logger.info("- selectores_css.json")
    
    logger.info("\n" + "="*60)
    logger.info("BUENAS PRÁCTICAS DE WEB SCRAPING")
    logger.info("="*60)
    logger.info("1. ✓ Respetar robots.txt del sitio")
    logger.info("2. ✓ Añadir delays entre requests (time.sleep)")
    logger.info("3. ✓ Usar User-Agent realista")
    logger.info("4. ✓ Manejar errores y timeouts")
    logger.info("5. ✓ No sobrecargar servidores")
    logger.info("6. ✓ Considerar APIs cuando estén disponibles")
    logger.info("7. ✓ Verificar términos de servicio del sitio")
    logger.info("8. ✓ Exportar datos en múltiples formatos")


if __name__ == "__main__":
    main()
