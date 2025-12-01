# Ejercicio 13: Expresiones Regulares - Búsqueda y Validación de Patrones
# Objetivo: Aprender a usar regex para validar, buscar y extraer datos

import re

# ===== PATRONES COMPILADOS =====
# Compilar patrones para reutilizar (más eficiente)

# Patrón para emails
patron_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

# Patrón para teléfonos (múltiples formatos)
patron_telefono = re.compile(r'^(\+?[\d\s\-\(\)]{7,15})$')

# Patrón para URLs
patron_url = re.compile(r'https?://[^\s]+')

# Patrón para fechas (DD/MM/YYYY)
patron_fecha = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')

# Patrón para contraseña fuerte
patron_contraseña = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

# ===== FUNCIONES DE VALIDACIÓN =====

def validar_email(email):
    """
    Valida formato de email
    Ejemplo: usuario@ejemplo.com
    """
    resultado = patron_email.match(email)
    return resultado is not None

def validar_telefono(telefono):
    """
    Valida formato de teléfono
    Ejemplos: +34 123 456 789, (123) 456-7890, etc.
    """
    resultado = patron_telefono.match(telefono)
    return resultado is not None

def validar_fecha(fecha_str):
    """
    Valida formato de fecha DD/MM/YYYY
    Retorna tupla (válido, dia, mes, año) o (False, None, None, None)
    """
    coincidencia = patron_fecha.match(fecha_str)
    if not coincidencia:
        return False, None, None, None
    
    dia, mes, año = coincidencia.groups()
    dia, mes, año = int(dia), int(mes), int(año)
    
    # Validar rangos
    if not (1 <= dia <= 31 and 1 <= mes <= 12 and año >= 1900):
        return False, None, None, None
    
    return True, dia, mes, año

def validar_contraseña(contraseña):
    """
    Valida contraseña fuerte:
    - Mínimo 8 caracteres
    - Al menos una mayúscula
    - Al menos una minúscula
    - Al menos un dígito
    - Al menos un carácter especial (@$!%*?&)
    """
    resultado = patron_contraseña.match(contraseña)
    return resultado is not None

def validar_url(url):
    """
    Valida formato de URL HTTP/HTTPS
    """
    resultado = patron_url.search(url)
    return resultado is not None

# ===== FUNCIONES DE BÚSQUEDA Y EXTRACCIÓN =====

def extraer_emails(texto):
    """
    Extrae todos los emails de un texto
    """
    patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(patron, texto)
    return emails

def extraer_numeros(texto):
    """
    Extrae todos los números del texto
    """
    numeros = re.findall(r'\d+', texto)
    return [int(n) for n in numeros]

def extraer_palabras(texto):
    """
    Extrae todas las palabras (sin números ni caracteres especiales)
    """
    palabras = re.findall(r'\b[a-zA-Z]+\b', texto)
    return palabras

def extraer_urls(texto):
    """
    Extrae todas las URLs de un texto
    """
    urls = re.findall(r'https?://[^\s]+', texto)
    return urls

def extraer_hashtags(texto):
    """
    Extrae todos los hashtags
    """
    hashtags = re.findall(r'#\w+', texto)
    return hashtags

def extraer_menciones(texto):
    """
    Extrae todas las menciones (@usuario)
    """
    menciones = re.findall(r'@\w+', texto)
    return menciones

# ===== FUNCIONES DE REEMPLAZO Y LIMPIEZA =====

def limpiar_espacios(texto):
    """
    Elimina espacios múltiples y normaliza espacios
    """
    # Reemplaza múltiples espacios por uno solo
    texto = re.sub(r'\s+', ' ', texto)
    # Elimina espacios al inicio y final
    return texto.strip()

def enmascarar_email(email):
    """
    Enmascara email: usuario@ejemplo.com -> u****o@ejemplo.com
    """
    patron = r'^(.)(.*?)(@.*)$'
    enmascado = re.sub(patron, r'\1****\3', email)
    return enmascado

def enmascarar_telefono(telefono):
    """
    Enmascara teléfono: 123456789 -> 123****789
    """
    patron = r'^(\d{3})(\d+)(\d{3})$'
    enmascarado = re.sub(patron, r'\1****\3', telefono.replace(' ', '').replace('-', ''))
    return enmascarado

def censurar_palabras(texto, palabras_censuradas):
    """
    Censura palabras reemplazándolas con asteriscos
    """
    for palabra in palabras_censuradas:
        # Usar IGNORECASE para no diferenciar mayúsculas
        patron = re.compile(re.escape(palabra), re.IGNORECASE)
        reemplazo = '*' * len(palabra)
        texto = patron.sub(reemplazo, texto)
    return texto

def convertir_markdown_a_html(texto):
    """
    Convierte markdown simple a HTML
    """
    # **texto** -> <strong>texto</strong>
    texto = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', texto)
    # *texto* -> <em>texto</em>
    texto = re.sub(r'\*(.*?)\*', r'<em>\1</em>', texto)
    # [enlace](url) -> <a href="url">enlace</a>
    texto = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', texto)
    return texto

# ===== FUNCIONES DE ANÁLISIS =====

def analizar_contraseña(contraseña):
    """
    Analiza la fortaleza de una contraseña
    """
    requisitos = {
        'minúsculas': bool(re.search(r'[a-z]', contraseña)),
        'mayúsculas': bool(re.search(r'[A-Z]', contraseña)),
        'dígitos': bool(re.search(r'\d', contraseña)),
        'caracteres especiales': bool(re.search(r'[@$!%*?&]', contraseña)),
        'longitud >= 8': len(contraseña) >= 8,
    }
    
    cumplidos = sum(requisitos.values())
    
    fortaleza = "Muy débil"
    if cumplidos >= 5:
        fortaleza = "Fuerte"
    elif cumplidos >= 4:
        fortaleza = "Buena"
    elif cumplidos >= 3:
        fortaleza = "Media"
    elif cumplidos >= 2:
        fortaleza = "Débil"
    
    return {
        'fortaleza': fortaleza,
        'requisitos': requisitos,
        'cumplidos': cumplidos,
        'total': len(requisitos)
    }

def encontrar_patrones(texto, patron_str):
    """
    Busca un patrón personalizado en texto
    Muestra coincidencias con posición
    """
    coincidencias = []
    for coincidencia in re.finditer(patron_str, texto):
        coincidencias.append({
            'texto': coincidencia.group(),
            'inicio': coincidencia.start(),
            'fin': coincidencia.end(),
            'grupo': coincidencia.group(1) if coincidencia.groups() else None
        })
    return coincidencias

# ===== MENÚ INTERACTIVO =====

def menu_expresiones_regulares():
    """Menú interactivo para demostrar regex"""
    
    while True:
        print("\n" + "="*60)
        print("=== EXPRESIONES REGULARES - BÚSQUEDA Y VALIDACIÓN ===")
        print("="*60)
        print("1. Validar email")
        print("2. Validar teléfono")
        print("3. Validar fecha (DD/MM/YYYY)")
        print("4. Validar contraseña fuerte")
        print("5. Validar URL")
        print("6. Extraer emails de texto")
        print("7. Extraer números de texto")
        print("8. Extraer palabras de texto")
        print("9. Extraer URLs de texto")
        print("10. Limpiar espacios múltiples")
        print("11. Enmascarar email")
        print("12. Enmascarar teléfono")
        print("13. Analizar fortaleza de contraseña")
        print("14. Buscar patrón personalizado")
        print("15. Salir")
        print("="*60)
        
        opcion = input("Elige una opción (1-15): ").strip()
        
        try:
            if opcion == "1":
                print("\n--- Validar Email ---")
                email = input("Ingresa email: ")
                if validar_email(email):
                    print(f"✓ '{email}' es un email válido")
                else:
                    print(f"✗ '{email}' NO es válido")
            
            elif opcion == "2":
                print("\n--- Validar Teléfono ---")
                print("Formatos válidos: +34 123 456 789, (123) 456-7890, 1234567890, etc.")
                telefono = input("Ingresa teléfono: ")
                if validar_telefono(telefono):
                    print(f"✓ '{telefono}' es válido")
                else:
                    print(f"✗ '{telefono}' NO es válido")
            
            elif opcion == "3":
                print("\n--- Validar Fecha ---")
                fecha = input("Ingresa fecha (DD/MM/YYYY): ")
                valido, dia, mes, año = validar_fecha(fecha)
                if valido:
                    print(f"✓ Fecha válida: {dia}/{mes}/{año}")
                else:
                    print(f"✗ Fecha inválida")
            
            elif opcion == "4":
                print("\n--- Validar Contraseña Fuerte ---")
                contraseña = input("Ingresa contraseña: ")
                if validar_contraseña(contraseña):
                    print(f"✓ Contraseña fuerte")
                else:
                    print(f"✗ Contraseña débil o no cumple requisitos")
                    analisis = analizar_contraseña(contraseña)
                    print(f"  Fortaleza: {analisis['fortaleza']}")
                    print(f"  Requisitos cumplidos: {analisis['cumplidos']}/{analisis['total']}")
            
            elif opcion == "5":
                print("\n--- Validar URL ---")
                url = input("Ingresa URL: ")
                if validar_url(url):
                    print(f"✓ '{url}' es una URL válida")
                else:
                    print(f"✗ '{url}' NO es válida")
            
            elif opcion == "6":
                print("\n--- Extraer Emails ---")
                texto = input("Ingresa texto: ")
                emails = extraer_emails(texto)
                if emails:
                    print(f"Emails encontrados: {emails}")
                else:
                    print("No se encontraron emails")
            
            elif opcion == "7":
                print("\n--- Extraer Números ---")
                texto = input("Ingresa texto: ")
                numeros = extraer_numeros(texto)
                if numeros:
                    print(f"Números encontrados: {numeros}")
                else:
                    print("No se encontraron números")
            
            elif opcion == "8":
                print("\n--- Extraer Palabras ---")
                texto = input("Ingresa texto: ")
                palabras = extraer_palabras(texto)
                if palabras:
                    print(f"Palabras encontradas: {palabras}")
                else:
                    print("No se encontraron palabras")
            
            elif opcion == "9":
                print("\n--- Extraer URLs ---")
                texto = input("Ingresa texto: ")
                urls = extraer_urls(texto)
                if urls:
                    print(f"URLs encontradas: {urls}")
                else:
                    print("No se encontraron URLs")
            
            elif opcion == "10":
                print("\n--- Limpiar Espacios ---")
                texto = input("Ingresa texto: ")
                limpio = limpiar_espacios(texto)
                print(f"Resultado: '{limpio}'")
            
            elif opcion == "11":
                print("\n--- Enmascarar Email ---")
                email = input("Ingresa email: ")
                enmascarado = enmascarar_email(email)
                print(f"Email enmascarado: {enmascarado}")
            
            elif opcion == "12":
                print("\n--- Enmascarar Teléfono ---")
                telefono = input("Ingresa teléfono (sin espacios): ")
                enmascarado = enmascarar_telefono(telefono)
                print(f"Teléfono enmascarado: {enmascarado}")
            
            elif opcion == "13":
                print("\n--- Analizar Fortaleza de Contraseña ---")
                contraseña = input("Ingresa contraseña: ")
                analisis = analizar_contraseña(contraseña)
                print(f"Fortaleza: {analisis['fortaleza']}")
                print(f"Requisitos: {analisis['cumplidos']}/{analisis['total']}")
                for req, cumplido in analisis['requisitos'].items():
                    estado = "✓" if cumplido else "✗"
                    print(f"  {estado} {req}")
            
            elif opcion == "14":
                print("\n--- Buscar Patrón Personalizado ---")
                texto = input("Ingresa texto: ")
                patron = input("Ingresa patrón regex: ")
                try:
                    coincidencias = encontrar_patrones(texto, patron)
                    if coincidencias:
                        print(f"Coincidencias encontradas: {len(coincidencias)}")
                        for i, match in enumerate(coincidencias, 1):
                            print(f"  {i}. '{match['texto']}' en posición {match['inicio']}-{match['fin']}")
                    else:
                        print("No se encontraron coincidencias")
                except re.error as e:
                    print(f"Error en patrón regex: {e}")
            
            elif opcion == "15":
                print("¡Hasta luego!")
                break
            
            else:
                print("Opción no válida")
        
        except Exception as e:
            print(f"Error: {e}")

# ===== PROGRAMA PRINCIPAL =====

if __name__ == "__main__":
    print("\n" + "="*60)
    print("BIENVENIDO AL SISTEMA DE EXPRESIONES REGULARES")
    print("="*60)
    
    # Demostraciones rápidas
    print("\n--- Demostraciones rápidas ---")
    
    print("\n1. Validación de emails:")
    emails_prueba = ["usuario@ejemplo.com", "invalido@", "correo@dominio.co.uk"]
    for email in emails_prueba:
        resultado = "✓" if validar_email(email) else "✗"
        print(f"  {resultado} {email}")
    
    print("\n2. Extracción de datos:")
    texto_ejemplo = "Contacta a juan@empresa.com o maria@empresa.com. Teléfono: 555-1234"
    print(f"  Texto: {texto_ejemplo}")
    print(f"  Emails: {extraer_emails(texto_ejemplo)}")
    print(f"  Números: {extraer_numeros(texto_ejemplo)}")
    
    print("\n3. Análisis de contraseña:")
    contraseña = "MiContraseña123!"
    analisis = analizar_contraseña(contraseña)
    print(f"  Contraseña: {contraseña}")
    print(f"  Fortaleza: {analisis['fortaleza']}")
    
    print("\n" + "="*60 + "\n")
    
    # Ejecutar menú
    menu_expresiones_regulares()

# === DESAFÍO ADICIONAL ===
# Crea un validador de números de tarjeta de crédito (Luhn algorithm)
# Implementa búsqueda de palabras clave en documentos
# Crea un limpiador de HTML que elimine tags
# Implementa un parser de comandos con patrones regex
