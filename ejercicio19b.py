"""
EJERCICIO 19B: Web Scraping Avanzado - Selenium para Sitios Dinámicos
Ejemplos de web scraping con JavaScript y contenido dinámico
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ScraperSelenium:
    """Clase para web scraping de sitios con JavaScript"""
    
    def __init__(self):
        """Inicializar el driver de Selenium (Chrome)"""
        self.driver = None
    
    def inicializar_driver(self):
        """
        Inicializar el navegador Chrome
        Nota: Requiere ChromeDriver descargado
        """
        try:
            # Opciones del navegador
            opciones = webdriver.ChromeOptions()
            opciones.add_argument('--start-maximized')
            # Descomentar para modo headless (sin interfaz gráfica)
            # opciones.add_argument('--headless')
            
            # Intenta crear el driver (requiere ChromeDriver en PATH)
            self.driver = webdriver.Chrome(options=opciones)
            logger.info("✓ Driver de Selenium inicializado")
            return True
        except Exception as e:
            logger.warning(f"⚠ ChromeDriver no disponible: {e}")
            logger.info("Para usar Selenium, descarga ChromeDriver desde:")
            logger.info("https://chromedriver.chromium.org/")
            return False
    
    def cerrar_driver(self):
        """Cerrar el navegador"""
        if self.driver:
            self.driver.quit()
            logger.info("Driver cerrado")
    
    def esperar_elemento(self, selector, timeout=10):
        """
        Esperar a que un elemento cargue (útil para sitios dinámicos)
        
        Args:
            selector (str): Selector CSS del elemento
            timeout (int): Tiempo máximo de espera en segundos
            
        Returns:
            WebElement: Elemento encontrado o None
        """
        try:
            elemento = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            logger.info(f"✓ Elemento encontrado: {selector}")
            return elemento
        except TimeoutException:
            logger.warning(f"⚠ Timeout esperando: {selector}")
            return None
    
    def simular_ejemplo_dinamico(self):
        """
        Ejemplo simulado de web scraping con contenido dinámico
        (No requiere conexión real)
        """
        logger.info("\n" + "="*60)
        logger.info("EJEMPLO: Scraping de contenido dinámico")
        logger.info("="*60)
        
        ejemplo = {
            'URL': 'https://ejemplo-dinamico.com',
            'Método': 'Selenium + WebDriverWait',
            'Pasos': [
                '1. Cargar página con JavaScript',
                '2. Esperar elemento específico',
                '3. Extraer datos del DOM modificado',
                '4. Manejar eventos (clicks, scroll)',
                '5. Guardar resultados'
            ],
            'Ventajas': [
                'Ejecuta JavaScript',
                'Maneja contenido dinámico',
                'Simula acciones de usuario',
                'Espera elementos con timeout'
            ],
            'Desventajas': [
                'Más lento que requests',
                'Requiere recursos del sistema',
                'Más difícil de mantener',
                'Puede detectarse más fácilmente'
            ]
        }
        
        for paso in ejemplo['Pasos']:
            logger.info(f"  {paso}")
        
        logger.info("\nVentajas de Selenium:")
        for ventaja in ejemplo['Ventajas']:
            logger.info(f"  • {ventaja}")
        
        logger.info("\nDesventajas de Selenium:")
        for desventaja in ejemplo['Desventajas']:
            logger.info(f"  • {desventaja}")
        
        return ejemplo


class PatronesAvanzados:
    """Patrones avanzados de web scraping"""
    
    @staticmethod
    def ejemplo_paginacion():
        """
        Ejemplo de scraping con paginación
        """
        logger.info("\n" + "="*60)
        logger.info("PATRÓN: Paginación")
        logger.info("="*60)
        
        codigo = '''
# Scraping de múltiples páginas
import requests
from bs4 import BeautifulSoup
import time

def scraping_paginado(url_base, num_paginas=5):
    datos = []
    
    for pagina in range(1, num_paginas + 1):
        url = f"{url_base}?page={pagina}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extraer datos de la página actual
        items = soup.find_all('div', class_='item')
        for item in items:
            titulo = item.find('h2').text
            precio = item.find('span', class_='precio').text
            datos.append({'titulo': titulo, 'precio': precio})
        
        logger.info(f"✓ Página {pagina} extraída ({len(items)} items)")
        time.sleep(2)  # Respetar servidor
    
    return datos
        '''
        logger.info(codigo)
        return codigo
    
    @staticmethod
    def ejemplo_autenticacion():
        """
        Ejemplo de scraping en sitios que requieren login
        """
        logger.info("\n" + "="*60)
        logger.info("PATRÓN: Autenticación (Login)")
        logger.info("="*60)
        
        codigo = '''
# Scraping con autenticación
import requests

session = requests.Session()

# Datos de login
credenciales = {
    'username': 'usuario@ejemplo.com',
    'password': 'contraseña'
}

# 1. Login
response = session.post('https://ejemplo.com/login', data=credenciales)

# 2. Ahora podemos acceder a páginas protegidas
response = session.get('https://ejemplo.com/datos-privados')
soup = BeautifulSoup(response.content, 'html.parser')

# Extraer datos de la página protegida
datos = soup.find_all('div', class_='contenido')
        '''
        logger.info(codigo)
        return codigo
    
    @staticmethod
    def ejemplo_manejo_errores():
        """
        Ejemplo de manejo robusto de errores
        """
        logger.info("\n" + "="*60)
        logger.info("PATRÓN: Manejo de Errores")
        logger.info("="*60)
        
        codigo = '''
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging

def crear_sesion_robusta():
    """Crear sesión con reintentos automáticos"""
    session = requests.Session()
    
    # Configurar reintentos
    retry = Retry(
        total=3,  # Número de reintentos
        backoff_factor=0.5,  # Espera entre reintentos
        status_forcelist=[500, 502, 503, 504]
    )
    
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    return session

# Usar la sesión
session = crear_sesion_robusta()

try:
    response = session.get('https://ejemplo.com', timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
except requests.exceptions.RequestException as e:
    logging.error(f"Error: {e}")
        '''
        logger.info(codigo)
        return codigo
    
    @staticmethod
    def ejemplo_multithreading():
        """
        Ejemplo de scraping multi-hilo para mayor velocidad
        """
        logger.info("\n" + "="*60)
        logger.info("PATRÓN: Multi-threading")
        logger.info("="*60)
        
        codigo = '''
import threading
import requests
from queue import Queue
from bs4 import BeautifulSoup

class ScraperMultihilo:
    def __init__(self, urls, num_workers=5):
        self.urls = urls
        self.num_workers = num_workers
        self.queue = Queue()
        self.resultados = []
    
    def worker(self):
        """Función ejecutada por cada hilo"""
        while not self.queue.empty():
            url = self.queue.get()
            try:
                response = requests.get(url, timeout=10)
                soup = BeautifulSoup(response.content, 'html.parser')
                titulo = soup.find('h1')
                if titulo:
                    self.resultados.append({
                        'url': url,
                        'titulo': titulo.text
                    })
            except Exception as e:
                logging.error(f"Error scraping {url}: {e}")
            finally:
                self.queue.task_done()
    
    def ejecutar(self):
        """Iniciar scraping multi-hilo"""
        # Llenar la cola
        for url in self.urls:
            self.queue.put(url)
        
        # Crear y iniciar hilos
        hilos = []
        for _ in range(self.num_workers):
            t = threading.Thread(target=self.worker)
            t.start()
            hilos.append(t)
        
        # Esperar a que se completen
        for t in hilos:
            t.join()
        
        return self.resultados
        '''
        logger.info(codigo)
        return codigo
    
    @staticmethod
    def ejemplo_cache():
        """
        Ejemplo de cacheo para evitar descargas repetidas
        """
        logger.info("\n" + "="*60)
        logger.info("PATRÓN: Cacheo de Datos")
        logger.info("="*60)
        
        codigo = '''
import requests
import json
import os
from datetime import datetime, timedelta

class ScraperConCache:
    def __init__(self, cache_dir='cache', cache_expiry=24):
        self.cache_dir = cache_dir
        self.cache_expiry = timedelta(hours=cache_expiry)
        os.makedirs(cache_dir, exist_ok=True)
    
    def obtener_cache_path(self, url):
        """Generar ruta del archivo de caché"""
        import hashlib
        hash_url = hashlib.md5(url.encode()).hexdigest()
        return os.path.join(self.cache_dir, f"{hash_url}.json")
    
    def cache_valido(self, cache_path):
        """Verificar si el caché es válido"""
        if not os.path.exists(cache_path):
            return False
        
        tiempo_cache = datetime.fromtimestamp(os.path.getmtime(cache_path))
        return datetime.now() - tiempo_cache < self.cache_expiry
    
    def obtener(self, url):
        """Obtener datos (del caché si está disponible)"""
        cache_path = self.obtener_cache_path(url)
        
        # Si hay caché válido, usarlo
        if self.cache_valido(cache_path):
            with open(cache_path, 'r') as f:
                return json.load(f)
        
        # Si no, descargar y cachear
        response = requests.get(url)
        datos = response.json()
        
        with open(cache_path, 'w') as f:
            json.dump(datos, f)
        
        return datos
        '''
        logger.info(codigo)
        return codigo


class MejoresPracticas:
    """Mejores prácticas y consideraciones legales"""
    
    @staticmethod
    def mostrar_guia():
        logger.info("\n" + "="*60)
        logger.info("✓ MEJORES PRÁCTICAS DE WEB SCRAPING")
        logger.info("="*60)
        
        practicas = {
            "RESPETO AL SERVIDOR": [
                "• Agregar delays entre requests (time.sleep)",
                "• Limitar velocidad de scraping",
                "• Usar delays progresivos",
                "• Implementar circuit breaker para errores"
            ],
            "IDENTIFICACIÓN": [
                "• Usar User-Agent realista",
                "• Incluir header 'Referer'",
                "• Respetar robots.txt",
                "• Considerar usar VPN si es necesario"
            ],
            "ROBUSTEZ": [
                "• Manejar timeouts",
                "• Reintentos con backoff exponencial",
                "• Validar datos extraídos",
                "• Registrar errores con logging"
            ],
            "ESCALABILIDAD": [
                "• Usar multi-threading/multiprocessing",
                "• Implementar cacheo",
                "• Usar colas para distribuir trabajo",
                "• Considerar bases de datos en lugar de archivos"
            ],
            "CONSIDERACIONES LEGALES": [
                "• Leer términos de servicio del sitio",
                "• Verificar permisos de uso de datos",
                "• Respetar copyright",
                "• Considerar usar APIs oficiales si existen"
            ],
            "HERRAMIENTAS ALTERNATIVAS": [
                "• Usar APIs oficiales (mejor opción)",
                "• Considerar Google Sheets para datos públicos",
                "• Usar Scrapy para proyectos grandes",
                "• Considerar servicios de scraping profesionales"
            ]
        }
        
        for categoria, items in practicas.items():
            logger.info(f"\n{categoria}:")
            for item in items:
                logger.info(f"  {item}")


def main():
    logger.info("\n" + "="*60)
    logger.info("EJERCICIO 19B: WEB SCRAPING AVANZADO")
    logger.info("="*60)
    
    # 1. Ejemplo de Selenium (si está disponible)
    logger.info("\n" + "-"*60)
    logger.info("1. Selenium para sitios dinámicos")
    logger.info("-"*60)
    
    scraper_selenium = ScraperSelenium()
    if scraper_selenium.inicializar_driver():
        scraper_selenium.simular_ejemplo_dinamico()
        scraper_selenium.cerrar_driver()
    else:
        scraper_selenium.simular_ejemplo_dinamico()
    
    # 2. Patrones avanzados
    logger.info("\n" + "-"*60)
    logger.info("2. Patrones de scraping avanzados")
    logger.info("-"*60)
    
    PatronesAvanzados.ejemplo_paginacion()
    PatronesAvanzados.ejemplo_autenticacion()
    PatronesAvanzados.ejemplo_manejo_errores()
    PatronesAvanzados.ejemplo_multithreading()
    PatronesAvanzados.ejemplo_cache()
    
    # 3. Mejores prácticas
    MejoresPracticas.mostrar_guia()
    
    logger.info("\n" + "="*60)
    logger.info("✓ EJERCICIO 19B COMPLETADO")
    logger.info("="*60)


if __name__ == "__main__":
    main()
