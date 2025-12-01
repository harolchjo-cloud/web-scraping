"""
EJERCICIO 19C: Ejemplos Prácticos Listos para Usar
Scripts que puedes copiar y adaptar a tus necesidades
"""

import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================================
# EJEMPLO 1: Scraper Básico con Manejo de Errores
# ============================================================================

class ScraperBasico:
    """Scraper robusto y reutilizable"""
    
    def __init__(self, delay=1):
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        })
    
    def obtener(self, url, max_reintentos=3):
        """Obtener página con reintentos"""
        for intento in range(max_reintentos):
            try:
                logger.info(f"Intento {intento+1}: GET {url}")
                response = self.session.get(url, timeout=10)
                response.raise_for_status()
                time.sleep(self.delay)
                return response.text
            except requests.RequestException as e:
                logger.warning(f"Error: {e}")
                if intento < max_reintentos - 1:
                    espera = 2 ** intento  # Backoff exponencial
                    logger.info(f"Reintentando en {espera} segundos...")
                    time.sleep(espera)
        return None


# ============================================================================
# EJEMPLO 2: Extractor de Tabla HTML
# ============================================================================

class ExtractorTabla:
    """Extraer tablas HTML y convertir a múltiples formatos"""
    
    @staticmethod
    def html_a_lista_diccionarios(html_tabla):
        """Convertir tabla HTML a lista de diccionarios"""
        soup = BeautifulSoup(html_tabla, 'html.parser')
        tabla = soup.find('table')
        
        if not tabla:
            return []
        
        # Extraer encabezados
        encabezados = []
        for th in tabla.find_all('th'):
            encabezados.append(th.text.strip())
        
        # Extraer filas
        datos = []
        for tr in tabla.find_all('tbody')[0].find_all('tr'):
            fila = {}
            celdas = tr.find_all('td')
            for i, celda in enumerate(celdas):
                if i < len(encabezados):
                    fila[encabezados[i]] = celda.text.strip()
            datos.append(fila)
        
        return datos
    
    @staticmethod
    def guardar_csv(datos, archivo):
        """Guardar datos en CSV"""
        if not datos:
            logger.warning("No hay datos para guardar")
            return
        
        with open(archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=datos[0].keys())
            writer.writeheader()
            writer.writerows(datos)
        logger.info(f"✓ Guardado en {archivo}")
    
    @staticmethod
    def guardar_json(datos, archivo):
        """Guardar datos en JSON"""
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        logger.info(f"✓ Guardado en {archivo}")


# ============================================================================
# EJEMPLO 3: Extractor de Producto (E-commerce)
# ============================================================================

class ExtractorProducto:
    """Extraer información de productos"""
    
    @staticmethod
    def extraer_precio(texto_precio):
        """Limpiar y convertir precio a float"""
        import re
        # Buscar números y puntos
        match = re.search(r'\d+[\.,]\d+', texto_precio)
        if match:
            precio = match.group(0).replace(',', '.')
            return float(precio)
        return None
    
    @staticmethod
    def extraer_puntuacion(texto_puntuacion):
        """Extraer puntuación de reseñas"""
        import re
        match = re.search(r'[\d.]+', texto_puntuacion)
        if match:
            return float(match.group(0))
        return None
    
    @staticmethod
    def scraping_productos_ejemplo():
        """
        Ejemplo: Scraping de 3 productos ficticios
        Puedes adaptar esto para un sitio real
        """
        html = '''
        <div class="producto">
            <h2>iPhone 15 Pro</h2>
            <span class="precio">$999.99</span>
            <div class="rating">4.8 / 5</div>
        </div>
        <div class="producto">
            <h2>Samsung S24</h2>
            <span class="precio">$899.99</span>
            <div class="rating">4.6 / 5</div>
        </div>
        <div class="producto">
            <h2>Google Pixel 8</h2>
            <span class="precio">$799.99</span>
            <div class="rating">4.5 / 5</div>
        </div>
        '''
        
        soup = BeautifulSoup(html, 'html.parser')
        productos = []
        
        for prod in soup.find_all('div', class_='producto'):
            nombre = prod.find('h2').text.strip()
            precio_texto = prod.find('span', class_='precio').text
            rating_texto = prod.find('div', class_='rating').text
            
            producto = {
                'nombre': nombre,
                'precio': ExtractorProducto.extraer_precio(precio_texto),
                'rating': ExtractorProducto.extraer_puntuacion(rating_texto),
                'fecha_extraccion': datetime.now().isoformat()
            }
            productos.append(producto)
            logger.info(f"✓ Extraído: {producto}")
        
        return productos


# ============================================================================
# EJEMPLO 4: Monitoreo de Cambios
# ============================================================================

class MonitorCambios:
    """Monitorear cambios en un sitio web"""
    
    def __init__(self, url, archivo_estado='estado.json'):
        self.url = url
        self.archivo_estado = archivo_estado
        self.estado_anterior = self.cargar_estado()
    
    def cargar_estado(self):
        """Cargar último estado guardado"""
        try:
            with open(self.archivo_estado, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return None
    
    def guardar_estado(self, datos):
        """Guardar estado actual"""
        with open(self.archivo_estado, 'w') as f:
            json.dump(datos, f)
    
    def detectar_cambios(self, datos_nuevos):
        """Comparar datos con estado anterior"""
        if self.estado_anterior is None:
            logger.info("📌 Primera ejecución - guardando estado")
            self.guardar_estado(datos_nuevos)
            return {"estado": "primera_vez"}
        
        cambios = []
        
        # Detectar elementos nuevos
        nuevos = [d for d in datos_nuevos if d not in self.estado_anterior]
        if nuevos:
            cambios.append(f"Elementos nuevos: {len(nuevos)}")
            logger.info(f"✨ {len(nuevos)} elementos nuevos")
        
        # Detectar elementos eliminados
        eliminados = [d for d in self.estado_anterior if d not in datos_nuevos]
        if eliminados:
            cambios.append(f"Elementos eliminados: {len(eliminados)}")
            logger.info(f"🗑️ {len(eliminados)} elementos eliminados")
        
        if cambios:
            self.guardar_estado(datos_nuevos)
            return {"cambios": cambios, "fecha": datetime.now().isoformat()}
        
        return {"cambios": []}


# ============================================================================
# EJEMPLO 5: Exportador de Datos
# ============================================================================

class ExportadorDatos:
    """Exportar datos en múltiples formatos"""
    
    @staticmethod
    def a_csv(datos, archivo):
        """Exportar a CSV"""
        if not datos:
            return
        with open(archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=datos[0].keys())
            writer.writeheader()
            writer.writerows(datos)
        logger.info(f"✓ Exportado a {archivo}")
    
    @staticmethod
    def a_json(datos, archivo):
        """Exportar a JSON"""
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        logger.info(f"✓ Exportado a {archivo}")
    
    @staticmethod
    def a_html(datos, archivo, titulo="Datos Extraídos"):
        """Exportar a HTML"""
        if not datos:
            return
        
        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>{titulo}</title>
            <style>
                body {{ font-family: Arial; margin: 20px; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
                th {{ background-color: #4CAF50; color: white; }}
                tr:nth-child(even) {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>{titulo}</h1>
            <table>
                <tr>
                    {''.join(f'<th>{col}</th>' for col in datos[0].keys())}
                </tr>
                {''.join(f'<tr>{"".join(f"<td>{row.get(col, "")}</td>" for col in datos[0].keys())}</tr>' for row in datos)}
            </table>
            <p><small>Generado: {datetime.now()}</small></p>
        </body>
        </html>
        '''
        
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(html)
        logger.info(f"✓ Exportado a {archivo}")


# ============================================================================
# EJEMPLO 6: Cleaner de Datos
# ============================================================================

class LimpiadorDatos:
    """Limpiar y validar datos extraídos"""
    
    @staticmethod
    def limpiar_texto(texto):
        """Limpiar espacios y caracteres especiales"""
        import re
        # Remover espacios extras
        texto = re.sub(r'\s+', ' ', texto)
        # Remover caracteres especiales si es necesario
        texto = texto.strip()
        return texto
    
    @staticmethod
    def validar_email(email):
        """Validar formato de email"""
        import re
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(patron, email))
    
    @staticmethod
    def validar_url(url):
        """Validar formato de URL"""
        import re
        patron = r'^https?://[\w\.-]+\.\w+.*$'
        return bool(re.match(patron, url))
    
    @staticmethod
    def procesar_datos(datos):
        """Procesar lista de diccionarios"""
        datos_limpios = []
        
        for item in datos:
            item_limpio = {}
            for clave, valor in item.items():
                if isinstance(valor, str):
                    item_limpio[clave] = LimpiadorDatos.limpiar_texto(valor)
                else:
                    item_limpio[clave] = valor
            datos_limpios.append(item_limpio)
        
        return datos_limpios


# ============================================================================
# EJEMPLO 7: Logger Personalizado
# ============================================================================

class LoggerScraping:
    """Logger para trackear scraping"""
    
    def __init__(self, archivo_log='scraping.log'):
        self.archivo_log = archivo_log
        self.log_file = open(archivo_log, 'a', encoding='utf-8')
    
    def registrar(self, evento, detalles):
        """Registrar evento de scraping"""
        entrada = {
            'timestamp': datetime.now().isoformat(),
            'evento': evento,
            'detalles': detalles
        }
        self.log_file.write(json.dumps(entrada, ensure_ascii=False) + '\n')
        self.log_file.flush()
        logger.info(f"[{evento}] {detalles}")
    
    def cerrar(self):
        """Cerrar archivo de log"""
        self.log_file.close()


# ============================================================================
# EJEMPLO 8: Pipeline Completo
# ============================================================================

class PipelineCompleto:
    """Pipeline completo: descargar → parsear → limpiar → guardar"""
    
    def __init__(self):
        self.scraper = ScraperBasico()
        self.logger = LoggerScraping()
    
    def ejecutar(self, url, selectores, nombre_archivo):
        """
        Ejecutar pipeline completo
        
        Args:
            url: URL a scrapear
            selectores: Dict con selectores CSS
            nombre_archivo: Nombre base para guardado
        """
        self.logger.registrar('inicio', f'Scraping de {url}')
        
        # 1. Descargar
        html = self.scraper.obtener(url)
        if not html:
            self.logger.registrar('error', 'No se pudo descargar la página')
            return
        
        self.logger.registrar('descarga', 'HTML descargado exitosamente')
        
        # 2. Parsear
        soup = BeautifulSoup(html, 'html.parser')
        datos = []
        
        for elemento in soup.select(selectores.get('principal', '')):
            item = {}
            for clave, selector in selectores.get('campos', {}).items():
                elem = elemento.select_one(selector)
                item[clave] = elem.text.strip() if elem else 'N/A'
            datos.append(item)
        
        self.logger.registrar('parseo', f'{len(datos)} elementos encontrados')
        
        # 3. Limpiar
        datos = LimpiadorDatos.procesar_datos(datos)
        self.logger.registrar('limpieza', 'Datos limpiados')
        
        # 4. Guardar
        ExportadorDatos.a_csv(datos, f'{nombre_archivo}.csv')
        ExportadorDatos.a_json(datos, f'{nombre_archivo}.json')
        ExportadorDatos.a_html(datos, f'{nombre_archivo}.html')
        
        self.logger.registrar('guardado', 'Archivos guardados')
        self.logger.cerrar()
        
        return datos


# ============================================================================
# DEMOSTRACIÓN
# ============================================================================

def main():
    logger.info("\n" + "="*60)
    logger.info("EJERCICIO 19C: Ejemplos Prácticos")
    logger.info("="*60)
    
    # Ejemplo 1: Scraper Básico
    logger.info("\n1. SCRAPER BÁSICO")
    logger.info("-" * 60)
    scraper = ScraperBasico()
    logger.info("✓ Scraper inicializado y listo para usar")
    
    # Ejemplo 2: Extractor de Tabla
    logger.info("\n2. EXTRACTOR DE TABLA")
    logger.info("-" * 60)
    html_tabla = """
    <table>
        <thead><tr><th>Producto</th><th>Precio</th></tr></thead>
        <tbody>
            <tr><td>Laptop</td><td>$999</td></tr>
            <tr><td>Mouse</td><td>$29</td></tr>
        </tbody>
    </table>
    """
    datos = ExtractorTabla.html_a_lista_diccionarios(html_tabla)
    ExtractorTabla.guardar_csv(datos, 'tabla_ejemplo.csv')
    ExtractorTabla.guardar_json(datos, 'tabla_ejemplo.json')
    
    # Ejemplo 3: Productos
    logger.info("\n3. SCRAPING DE PRODUCTOS")
    logger.info("-" * 60)
    productos = ExtractorProducto.scraping_productos_ejemplo()
    ExportadorDatos.a_csv(productos, 'productos_ejemplo.csv')
    ExportadorDatos.a_json(productos, 'productos_ejemplo.json')
    
    # Ejemplo 4: Cleaner
    logger.info("\n4. LIMPIEZA DE DATOS")
    logger.info("-" * 60)
    datos_limpios = LimpiadorDatos.procesar_datos(productos)
    logger.info(f"✓ {len(datos_limpios)} items limpiados")
    
    # Ejemplo 5: Validación
    logger.info("\n5. VALIDACIÓN DE DATOS")
    logger.info("-" * 60)
    es_email_valido = LimpiadorDatos.validar_email('usuario@ejemplo.com')
    es_url_valida = LimpiadorDatos.validar_url('https://www.ejemplo.com')
    logger.info(f"Email válido: {es_email_valido}")
    logger.info(f"URL válida: {es_url_valida}")
    
    logger.info("\n" + "="*60)
    logger.info("✓ DEMOSTRACIÓN COMPLETADA")
    logger.info("="*60)
    logger.info("\nArchivos generados:")
    logger.info("- tabla_ejemplo.csv / .json")
    logger.info("- productos_ejemplo.csv / .json")
    logger.info("- scraping.log")


if __name__ == "__main__":
    main()
