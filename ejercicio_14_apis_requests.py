# Ejercicio 14: APIs y Requests - Comunicación con Servicios Web
# Objetivo: Aprender a comunicarse con APIs usando HTTP requests

import requests
import json
from datetime import datetime
import time

# ===== CONSTANTES =====

# APIs públicas gratuitas (sin autenticación requerida)
API_WEATHER = "https://api.open-meteo.com/v1/forecast"  # Clima
API_POKEAPI = "https://pokeapi.co/api/v2"  # Pokémon
API_JSONPLACEHOLDER = "https://jsonplaceholder.typicode.com"  # Fake API para testing
API_RANDOM_USER = "https://randomuser.me/api"  # Usuarios aleatorios
API_DOG_FACTS = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs"  # Datos sobre perros
API_JOKE = "https://api.chucknorris.io/jokes/random"  # Chistes de Chuck Norris

# Tiempos de espera (timeout)
TIMEOUT = 5

# ===== FUNCIONES DE PETICIONES BÁSICAS =====

def hacer_peticion_get(url, params=None, headers=None):
    """
    Realiza una petición GET a una URL
    Args:
        url: URL a donde hacer la petición
        params: Parámetros de consulta (dict)
        headers: Encabezados HTTP (dict)
    Returns:
        Diccionario con respuesta o error
    """
    try:
        respuesta = requests.get(url, params=params, headers=headers, timeout=TIMEOUT)
        respuesta.raise_for_status()  # Lanza excepción si hay error HTTP
        
        return {
            'exitoso': True,
            'estado': respuesta.status_code,
            'datos': respuesta.json() if respuesta.text else respuesta.text,
            'encabezados': dict(respuesta.headers)
        }
    
    except requests.exceptions.Timeout:
        return {
            'exitoso': False,
            'error': 'Tiempo de espera agotado',
            'estado': None
        }
    except requests.exceptions.ConnectionError:
        return {
            'exitoso': False,
            'error': 'Error de conexión',
            'estado': None
        }
    except requests.exceptions.HTTPError as e:
        return {
            'exitoso': False,
            'error': f'Error HTTP: {e}',
            'estado': respuesta.status_code
        }
    except ValueError:
        return {
            'exitoso': False,
            'error': 'Respuesta no es JSON válido',
            'estado': respuesta.status_code
        }
    except Exception as e:
        return {
            'exitoso': False,
            'error': f'Error inesperado: {e}',
            'estado': None
        }

def hacer_peticion_post(url, datos=None, json_data=None, headers=None):
    """
    Realiza una petición POST a una URL
    """
    try:
        respuesta = requests.post(
            url,
            data=datos,
            json=json_data,
            headers=headers,
            timeout=TIMEOUT
        )
        respuesta.raise_for_status()
        
        return {
            'exitoso': True,
            'estado': respuesta.status_code,
            'datos': respuesta.json() if respuesta.text else respuesta.text
        }
    
    except Exception as e:
        return {
            'exitoso': False,
            'error': str(e),
            'estado': None
        }

# ===== FUNCIONES DE APIS ESPECÍFICAS =====

def obtener_clima(latitud, longitud):
    """
    Obtiene datos meteorológicos para una ubicación específica
    Usa Open-Meteo API (gratuita, sin clave requerida)
    """
    params = {
        'latitude': latitud,
        'longitude': longitud,
        'current': 'temperature_2m,relative_humidity_2m,weather_code',
        'timezone': 'auto'
    }
    
    resultado = hacer_peticion_get(API_WEATHER, params=params)
    
    if resultado['exitoso']:
        datos = resultado['datos']
        clima = datos.get('current', {})
        return {
            'exitoso': True,
            'temperatura': clima.get('temperature_2m'),
            'humedad': clima.get('relative_humidity_2m'),
            'codigo_clima': clima.get('weather_code'),
            'zona_horaria': datos.get('timezone')
        }
    
    return resultado

def obtener_pokemon(nombre_id):
    """
    Obtiene información de un Pokémon
    """
    url = f"{API_POKEAPI}/pokemon/{nombre_id.lower()}"
    resultado = hacer_peticion_get(url)
    
    if resultado['exitoso']:
        datos = resultado['datos']
        return {
            'exitoso': True,
            'nombre': datos.get('name'),
            'id': datos.get('id'),
            'peso': datos.get('weight'),
            'altura': datos.get('height'),
            'tipos': [tipo['type']['name'] for tipo in datos.get('types', [])],
            'habilidades': [hab['ability']['name'] for hab in datos.get('abilities', [])]
        }
    
    return resultado

def obtener_usuario_aleatorio():
    """
    Obtiene datos de un usuario aleatorio
    """
    resultado = hacer_peticion_get(API_RANDOM_USER)
    
    if resultado['exitoso']:
        usuario = resultado['datos']['results'][0]
        return {
            'exitoso': True,
            'nombre': f"{usuario['name']['first']} {usuario['name']['last']}",
            'email': usuario['email'],
            'telefono': usuario['phone'],
            'pais': usuario['location']['country'],
            'foto': usuario['picture']['large']
        }
    
    return resultado

def obtener_chiste():
    """
    Obtiene un chiste aleatorio de Chuck Norris
    """
    resultado = hacer_peticion_get(API_JOKE)
    
    if resultado['exitoso']:
        datos = resultado['datos']
        return {
            'exitoso': True,
            'chiste': datos.get('value'),
            'categoria': datos.get('categories')
        }
    
    return resultado

def obtener_posts_fake():
    """
    Obtiene posts de una API fake (JSONPlaceholder)
    """
    url = f"{API_JSONPLACEHOLDER}/posts"
    params = {'_limit': 5}  # Limita a 5 resultados
    
    resultado = hacer_peticion_get(url, params=params)
    
    if resultado['exitoso']:
        posts = resultado['datos']
        return {
            'exitoso': True,
            'cantidad': len(posts),
            'posts': posts
        }
    
    return resultado

def crear_post_fake(titulo, cuerpo, user_id=1):
    """
    Crea un post en JSONPlaceholder (API fake)
    """
    url = f"{API_JSONPLACEHOLDER}/posts"
    datos = {
        'title': titulo,
        'body': cuerpo,
        'userId': user_id
    }
    
    resultado = hacer_peticion_post(url, json_data=datos)
    
    if resultado['exitoso']:
        return {
            'exitoso': True,
            'id': resultado['datos'].get('id'),
            'mensaje': 'Post creado exitosamente'
        }
    
    return resultado

# ===== FUNCIÓN PARA PROBAR CÓDIGOS HTTP =====

def demostrar_codigos_http():
    """
    Demuestra diferentes códigos de estado HTTP
    """
    print("\n=== CÓDIGOS DE ESTADO HTTP ===")
    
    casos_prueba = [
        (f"{API_JSONPLACEHOLDER}/posts/1", 200, "GET exitoso"),
        (f"{API_JSONPLACEHOLDER}/posts/999999", 404, "Recurso no encontrado"),
        ("https://httpstat.us/500", 500, "Error del servidor"),
    ]
    
    for url, codigo_esperado, descripcion in casos_prueba:
        try:
            resp = requests.get(url, timeout=3)
            print(f"{resp.status_code} - {descripcion}: {url}")
        except Exception as e:
            print(f"Error - {descripcion}: {e}")

# ===== FUNCIÓN DE MANEJO DE SESIONES =====

def demostrar_sesiones():
    """
    Demuestra el uso de sesiones para múltiples peticiones
    """
    print("\n=== USANDO SESIONES ===")
    
    sesion = requests.Session()
    
    # Las cookies y configuración se mantienen entre peticiones
    respuesta1 = sesion.get(f"{API_JSONPLACEHOLDER}/posts/1")
    respuesta2 = sesion.get(f"{API_JSONPLACEHOLDER}/posts/2")
    
    print(f"Post 1: {respuesta1.json().get('title')}")
    print(f"Post 2: {respuesta2.json().get('title')}")
    
    sesion.close()

# ===== MENÚ INTERACTIVO =====

def menu_apis():
    """Menú interactivo para probar APIs"""
    
    while True:
        print("\n" + "="*60)
        print("=== CLIENTE DE APIs - COMUNICACIÓN WEB ===")
        print("="*60)
        print("1. Obtener clima de una ubicación")
        print("2. Obtener información de un Pokémon")
        print("3. Obtener usuario aleatorio")
        print("4. Obtener chiste de Chuck Norris")
        print("5. Obtener posts de API fake")
        print("6. Crear un post en API fake")
        print("7. Demostrar códigos HTTP")
        print("8. Demostrar sesiones")
        print("9. Ver headers de respuesta")
        print("10. Salir")
        print("="*60)
        
        opcion = input("Elige una opción (1-10): ").strip()
        
        try:
            if opcion == "1":
                print("\n--- Obtener Clima ---")
                print("Ejemplos: Madrid (40.4168, -3.7038), Nueva York (40.7128, -74.0060)")
                lat = float(input("Latitud: "))
                lon = float(input("Longitud: "))
                
                resultado = obtener_clima(lat, lon)
                if resultado['exitoso']:
                    print(f"\n✓ Datos obtenidos:")
                    print(f"  Temperatura: {resultado['temperatura']}°C")
                    print(f"  Humedad: {resultado['humedad']}%")
                    print(f"  Zona horaria: {resultado['zona_horaria']}")
                else:
                    print(f"✗ Error: {resultado['error']}")
            
            elif opcion == "2":
                print("\n--- Obtener Pokémon ---")
                pokemon = input("Nombre o ID del Pokémon (ej: pikachu, 1): ")
                
                resultado = obtener_pokemon(pokemon)
                if resultado['exitoso']:
                    print(f"\n✓ {resultado['nombre'].title()}")
                    print(f"  ID: {resultado['id']}")
                    print(f"  Tipos: {', '.join(resultado['tipos'])}")
                    print(f"  Habilidades: {', '.join(resultado['habilidades'])}")
                else:
                    print(f"✗ Error: {resultado['error']}")
            
            elif opcion == "3":
                print("\n--- Usuario Aleatorio ---")
                
                resultado = obtener_usuario_aleatorio()
                if resultado['exitoso']:
                    print(f"\n✓ Datos obtenidos:")
                    print(f"  Nombre: {resultado['nombre']}")
                    print(f"  Email: {resultado['email']}")
                    print(f"  Teléfono: {resultado['telefono']}")
                    print(f"  País: {resultado['pais']}")
                else:
                    print(f"✗ Error: {resultado['error']}")
            
            elif opcion == "4":
                print("\n--- Chiste Aleatorio ---")
                
                resultado = obtener_chiste()
                if resultado['exitoso']:
                    print(f"\n✓ {resultado['chiste']}")
                    if resultado['categoria']:
                        print(f"  Categoría: {', '.join(resultado['categoria'])}")
                else:
                    print(f"✗ Error: {resultado['error']}")
            
            elif opcion == "5":
                print("\n--- Posts de API Fake ---")
                
                resultado = obtener_posts_fake()
                if resultado['exitoso']:
                    print(f"\n✓ Se obtuvieron {resultado['cantidad']} posts:")
                    for post in resultado['posts']:
                        print(f"\n  Post #{post['id']}: {post['title']}")
                        print(f"  {post['body'][:100]}...")
                else:
                    print(f"✗ Error: {resultado['error']}")
            
            elif opcion == "6":
                print("\n--- Crear Post en API Fake ---")
                titulo = input("Título del post: ")
                cuerpo = input("Contenido del post: ")
                
                resultado = crear_post_fake(titulo, cuerpo)
                if resultado['exitoso']:
                    print(f"\n✓ {resultado['mensaje']}")
                    print(f"  ID asignado: {resultado['id']}")
                else:
                    print(f"✗ Error: {resultado['error']}")
            
            elif opcion == "7":
                demostrar_codigos_http()
            
            elif opcion == "8":
                demostrar_sesiones()
            
            elif opcion == "9":
                print("\n--- Headers de Respuesta ---")
                url = input("Ingresa una URL (o deja en blanco para un default): ").strip()
                if not url:
                    url = f"{API_JSONPLACEHOLDER}/posts/1"
                
                resultado = hacer_peticion_get(url)
                if resultado['exitoso']:
                    print("\n✓ Headers:")
                    for clave, valor in resultado['encabezados'].items():
                        print(f"  {clave}: {valor}")
                else:
                    print(f"✗ Error: {resultado['error']}")
            
            elif opcion == "10":
                print("¡Hasta luego!")
                break
            
            else:
                print("Opción no válida")
        
        except ValueError:
            print("❌ Error: Ingresa valores válidos")
        except Exception as e:
            print(f"❌ Error: {e}")

# ===== PROGRAMA PRINCIPAL =====

if __name__ == "__main__":
    print("\n" + "="*60)
    print("BIENVENIDO AL CLIENTE DE APIs")
    print("="*60)
    
    # Demostraciones rápidas
    print("\n--- Demostraciones rápidas ---")
    
    print("\n1. Obtener Pokémon (Pikachu):")
    resultado = obtener_pokemon("pikachu")
    if resultado['exitoso']:
        print(f"  ✓ {resultado['nombre'].title()} - Tipos: {', '.join(resultado['tipos'])}")
    else:
        print(f"  ✗ {resultado['error']}")
    
    print("\n2. Obtener Chiste:")
    resultado = obtener_chiste()
    if resultado['exitoso']:
        print(f"  ✓ {resultado['chiste'][:80]}...")
    else:
        print(f"  ✗ {resultado['error']}")
    
    print("\n3. Clima (Madrid):")
    resultado = obtener_clima(40.4168, -3.7038)
    if resultado['exitoso']:
        print(f"  ✓ Temperatura: {resultado['temperatura']}°C")
    else:
        print(f"  ✗ {resultado['error']}")
    
    print("\n" + "="*60 + "\n")
    
    # Ejecutar menú
    menu_apis()

# === DESAFÍO ADICIONAL ===
# Crea un cliente de GitHub API
# Implementa autenticación con token Bearer
# Crea un scraper de datos con requests y Beautiful Soup
# Implementa manejo de rate limiting
# Crea un cliente de OpenWeatherMap con autenticación
