# Ejercicio 10: Manejo de Excepciones - Control de Errores Robusto
# Objetivo: Aprender a manejar errores de forma elegante y profesional

from pathlib import Path

# Excepciones personalizadas
class ErrorEdadInvalida(Exception):
    """Excepción personalizada para edades inválidas"""
    pass

class ErrorArchivo(Exception):
    """Excepción personalizada para errores de archivo"""
    pass

# Función: Calculadora segura con manejo de errores
def calculadora_segura(a, b, operacion):
    """
    Realiza operaciones matemáticas de forma segura
    Args:
        a, b: Números a operar
        operacion: '+', '-', '*', '/'
    """
    try:
        a = float(a)
        b = float(b)
        
        if operacion == '+':
            resultado = a + b
        elif operacion == '-':
            resultado = a - b
        elif operacion == '*':
            resultado = a * b
        elif operacion == '/':
            if b == 0:
                raise ZeroDivisionError("No se puede dividir entre cero")
            resultado = a / b
        else:
            raise ValueError(f"Operación '{operacion}' no válida")
        
        return round(resultado, 2)
    
    except ValueError as e:
        print(f"Error de valor: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"Error matemático: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None
    finally:
        print("Operación completada (o falló)\n")

# Función: Validador de datos de usuario
def validar_edad(edad_str):
    """
    Valida que la edad sea un número válido y positivo
    Lanza excepciones personalizadas
    """
    try:
        edad = int(edad_str)
        
        if edad < 0:
            raise ErrorEdadInvalida("La edad no puede ser negativa")
        if edad > 150:
            raise ErrorEdadInvalida("La edad parece demasiado alta")
        if edad < 13:
            raise ErrorEdadInvalida("Debes tener al menos 13 años")
        
        return edad
    
    except ValueError:
        raise ErrorEdadInvalida("La edad debe ser un número entero")

# Función: Convertidor de tipos seguro
def convertir_tipo(valor, tipo_destino):
    """
    Convierte un valor a un tipo específico con manejo de errores
    """
    try:
        if tipo_destino == "int":
            return int(valor)
        elif tipo_destino == "float":
            return float(valor)
        elif tipo_destino == "bool":
            if valor.lower() in ["si", "true", "1", "verdadero"]:
                return True
            elif valor.lower() in ["no", "false", "0", "falso"]:
                return False
            else:
                raise ValueError("Valor booleano no válido")
        else:
            raise TypeError(f"Tipo '{tipo_destino}' no soportado")
    
    except ValueError as e:
        print(f"Error de conversión: No se pudo convertir '{valor}' a {tipo_destino}")
        return None
    except TypeError as e:
        print(f"Error de tipo: {e}")
        return None

# Función: Gestor de archivos con manejo de errores
def leer_archivo_seguro(nombre_archivo):
    """
    Lee un archivo de forma segura con validaciones
    """
    ruta = Path(nombre_archivo)
    
    try:
        if not ruta.exists():
            raise FileNotFoundError(f"El archivo '{nombre_archivo}' no existe")
        
        if not ruta.is_file():
            raise ErrorArchivo(f"'{nombre_archivo}' no es un archivo válido")
        
        with open(ruta, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            return contenido
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except PermissionError:
        print(f"Error: No tienes permisos para acceder a '{nombre_archivo}'")
        return None
    except ErrorArchivo as e:
        print(f"Error personalizado: {e}")
        return None
    except Exception as e:
        print(f"Error desconocido: {e}")
        return None

# Función: Procesa lista de números con validación
def procesar_lista_numeros(numeros_str):
    """
    Convierte string a lista de números con manejo de errores
    """
    try:
        numeros = []
        for elemento in numeros_str.split(","):
            numero = float(elemento.strip())
            numeros.append(numero)
        
        if not numeros:
            raise ValueError("La lista de números está vacía")
        
        return numeros
    
    except ValueError as e:
        print(f"Error al procesar números: {e}")
        return None

# Función: Menú interactivo principal
def menu_excepciones():
    """Menú interactivo para probar el manejo de excepciones"""
    
    while True:
        print("=" * 50)
        print("=== MANEJO DE EXCEPCIONES ===")
        print("=" * 50)
        print("1. Calculadora segura")
        print("2. Validar edad")
        print("3. Convertir tipo de dato")
        print("4. Leer archivo")
        print("5. Procesar lista de números")
        print("6. Salir")
        print("=" * 50)
        
        opcion = input("Elige una opción (1-6): ").strip()
        
        try:
            if opcion == "1":
                print("\n--- Calculadora Segura ---")
                a = input("Primer número: ")
                b = input("Segundo número: ")
                operacion = input("Operación (+, -, *, /): ")
                resultado = calculadora_segura(a, b, operacion)
                if resultado is not None:
                    print(f"Resultado: {resultado}\n")
            
            elif opcion == "2":
                print("\n--- Validador de Edad ---")
                try:
                    edad_input = input("Ingresa tu edad: ")
                    edad = validar_edad(edad_input)
                    print(f"✓ Edad válida: {edad} años\n")
                except ErrorEdadInvalida as e:
                    print(f"✗ Error: {e}\n")
            
            elif opcion == "3":
                print("\n--- Convertidor de Tipos ---")
                valor = input("Ingresa un valor: ")
                tipo = input("Tipo destino (int, float, bool): ")
                resultado = convertir_tipo(valor, tipo)
                if resultado is not None:
                    print(f"✓ Conversión exitosa: {resultado} ({type(resultado).__name__})\n")
            
            elif opcion == "4":
                print("\n--- Lector de Archivos ---")
                nombre = input("Nombre del archivo: ")
                contenido = leer_archivo_seguro(nombre)
                if contenido:
                    print(f"✓ Archivo leído correctamente:")
                    print(contenido[:200] + "..." if len(contenido) > 200 else contenido)
                    print()
            
            elif opcion == "5":
                print("\n--- Procesador de Números ---")
                numeros_str = input("Ingresa números separados por comas: ")
                numeros = procesar_lista_numeros(numeros_str)
                if numeros:
                    print(f"✓ Números procesados: {numeros}")
                    print(f"  Suma: {sum(numeros)}")
                    print(f"  Promedio: {sum(numeros) / len(numeros):.2f}\n")
            
            elif opcion == "6":
                print("¡Hasta luego!")
                break
            
            else:
                raise ValueError("Opción no válida")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Programa interrumpido por el usuario")
            break
        except Exception as e:
            print(f"Error no esperado: {e}\n")

# Programa principal
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("BIENVENIDO AL SISTEMA DE MANEJO DE EXCEPCIONES")
    print("=" * 50 + "\n")
    
    # Demostración rápida
    print("--- Demostraciones rápidas ---")
    print("\n1. Calculadora:")
    resultado = calculadora_segura("10", "2", "/")
    if resultado:
        print(f"10 / 2 = {resultado}")
    
    print("\n2. División por cero:")
    resultado = calculadora_segura("5", "0", "/")
    
    print("\n3. Conversión de tipos:")
    num = convertir_tipo("42.5", "int")
    if num:
        print(f"Conversión exitosa: {num}")
    
    print("\n" + "=" * 50 + "\n")
    
    # Ejecutar menú interactivo
    menu_excepciones()

# === DESAFÍO ADICIONAL ===
# Crea una función que valide direcciones de email
# Crea una función que maneje descargas de archivos
# Agrega más tipos de excepciones personalizadas
# Crea un registro de errores (log) en un archivo
