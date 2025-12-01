# Ejercicio 18: Automatización de Tareas - Scripts y Scheduling
# Objetivo: Aprender a automatizar tareas repetitivas con Python

import os
import shutil
import schedule
import time
import psutil
import logging
import json
import glob
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ===== CONFIGURACIÓN DE LOGGING =====

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('automatizacion.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ===== CONFIGURACIÓN =====

DIRECTORIO_MONITOREO = './archivos_monitoreados'
DIRECTORIO_RESPALDO = './respaldos'
DIRECTORIO_TEMP = './temp'
DIRECTORIO_REPORTES = './reportes'
ARCHIVOS_ANTIGUOS_DIAS = 30

# ===== FUNCIONES DE SISTEMA DE ARCHIVOS =====

class GestorArchivos:
    """Gestiona operaciones con archivos y directorios"""
    
    @staticmethod
    def crear_directorio(ruta):
        """Crea un directorio si no existe"""
        try:
            Path(ruta).mkdir(parents=True, exist_ok=True)
            logger.info(f"Directorio verificado/creado: {ruta}")
            return True
        except Exception as e:
            logger.error(f"Error al crear directorio {ruta}: {e}")
            return False
    
    @staticmethod
    def listar_archivos(directorio, extension=None):
        """
        Lista archivos en un directorio
        
        Args:
            directorio: Ruta del directorio
            extension: Filtrar por extensión (ej: '.txt')
        
        Returns:
            Lista de archivos
        """
        try:
            if extension:
                patron = os.path.join(directorio, f'*{extension}')
                return glob.glob(patron)
            else:
                return os.listdir(directorio)
        except Exception as e:
            logger.error(f"Error al listar archivos: {e}")
            return []
    
    @staticmethod
    def obtener_tamaño_archivo(ruta):
        """Obtiene tamaño de archivo en bytes"""
        try:
            return os.path.getsize(ruta)
        except Exception as e:
            logger.error(f"Error al obtener tamaño: {e}")
            return 0
    
    @staticmethod
    def obtener_fecha_modificacion(ruta):
        """Obtiene fecha de última modificación"""
        try:
            timestamp = os.path.getmtime(ruta)
            return datetime.fromtimestamp(timestamp)
        except Exception as e:
            logger.error(f"Error al obtener fecha: {e}")
            return None
    
    @staticmethod
    def obtener_antiguedad_dias(ruta):
        """Obtiene antiguedad de archivo en días"""
        try:
            fecha_mod = GestorArchivos.obtener_fecha_modificacion(ruta)
            if fecha_mod:
                antiguedad = datetime.now() - fecha_mod
                return antiguedad.days
            return None
        except Exception as e:
            logger.error(f"Error al calcular antiguedad: {e}")
            return None
    
    @staticmethod
    def mover_archivo(origen, destino):
        """Mueve un archivo de un lugar a otro"""
        try:
            shutil.move(origen, destino)
            logger.info(f"Archivo movido: {origen} -> {destino}")
            return True
        except Exception as e:
            logger.error(f"Error al mover archivo: {e}")
            return False
    
    @staticmethod
    def copiar_archivo(origen, destino):
        """Copia un archivo"""
        try:
            shutil.copy2(origen, destino)
            logger.info(f"Archivo copiado: {origen} -> {destino}")
            return True
        except Exception as e:
            logger.error(f"Error al copiar archivo: {e}")
            return False
    
    @staticmethod
    def eliminar_archivo(ruta):
        """Elimina un archivo"""
        try:
            os.remove(ruta)
            logger.info(f"Archivo eliminado: {ruta}")
            return True
        except Exception as e:
            logger.error(f"Error al eliminar archivo: {e}")
            return False
    
    @staticmethod
    def recorrer_directorio_recursivo(directorio):
        """Recorre directorios de forma recursiva (os.walk)"""
        archivos = []
        try:
            for root, dirs, files in os.walk(directorio):
                for file in files:
                    ruta_completa = os.path.join(root, file)
                    archivos.append({
                        'ruta': ruta_completa,
                        'nombre': file,
                        'tamaño': GestorArchivos.obtener_tamaño_archivo(ruta_completa),
                        'modificado': GestorArchivos.obtener_fecha_modificacion(ruta_completa)
                    })
        except Exception as e:
            logger.error(f"Error al recorrer directorio: {e}")
        
        return archivos

# ===== FUNCIONES DE LIMPIEZA =====

class LimpiadorArchivos:
    """Limpia archivos según criterios"""
    
    @staticmethod
    def limpiar_archivos_antiguos(directorio, dias=ARCHIVOS_ANTIGUOS_DIAS):
        """
        Elimina archivos más antiguos que X días
        
        Args:
            directorio: Directorio a limpiar
            dias: Antiguedad mínima en días
        """
        print(f"\n=== LIMPIANDO ARCHIVOS MÁS ANTIGUOS DE {dias} DÍAS ===\n")
        
        try:
            archivos = GestorArchivos.recorrer_directorio_recursivo(directorio)
            eliminados = 0
            
            for archivo_info in archivos:
                antiguedad = GestorArchivos.obtener_antiguedad_dias(archivo_info['ruta'])
                
                if antiguedad and antiguedad > dias:
                    if GestorArchivos.eliminar_archivo(archivo_info['ruta']):
                        eliminados += 1
            
            logger.info(f"Limpieza completada: {eliminados} archivos eliminados")
            print(f"✓ {eliminados} archivos eliminados\n")
            
        except Exception as e:
            logger.error(f"Error en limpieza: {e}")
    
    @staticmethod
    def limpiar_archivos_temporales():
        """Limpia archivos temporales"""
        print("\n=== LIMPIANDO ARCHIVOS TEMPORALES ===\n")
        
        extensiones_temp = ['.tmp', '.temp', '.log', '.cache']
        eliminados = 0
        
        for ext in extensiones_temp:
            archivos = GestorArchivos.listar_archivos(DIRECTORIO_TEMP, ext)
            for archivo in archivos:
                if GestorArchivos.eliminar_archivo(archivo):
                    eliminados += 1
        
        print(f"✓ {eliminados} archivos temporales eliminados\n")
    
    @staticmethod
    def limpiar_espacio_disco(minimo_mb=100):
        """
        Advierte si el espacio en disco es bajo
        
        Args:
            minimo_mb: Espacio mínimo en MB
        """
        try:
            disco = shutil.disk_usage('/')
            espacio_libre_mb = disco.free / (1024 * 1024)
            
            if espacio_libre_mb < minimo_mb:
                mensaje = f"⚠ Espacio en disco bajo: {espacio_libre_mb:.2f} MB"
                logger.warning(mensaje)
                print(f"\n{mensaje}\n")
            else:
                print(f"\n✓ Espacio en disco adecuado: {espacio_libre_mb:.2f} MB\n")
        
        except Exception as e:
            logger.error(f"Error al verificar espacio: {e}")

# ===== FUNCIONES DE RESPALDO =====

class GestorRespaldos:
    """Gestiona respaldos automáticos"""
    
    @staticmethod
    def crear_respaldo(directorio_origen, directorio_respaldo):
        """
        Crea respaldo de un directorio
        
        Args:
            directorio_origen: Directorio a respaldar
            directorio_respaldo: Donde guardar el respaldo
        """
        print(f"\n=== CREANDO RESPALDO ===\n")
        
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            nombre_respaldo = f"respaldo_{timestamp}"
            ruta_respaldo = os.path.join(directorio_respaldo, nombre_respaldo)
            
            # Crear respaldo
            shutil.copytree(directorio_origen, ruta_respaldo)
            
            tamaño = GestorArchivos.obtener_tamaño_archivo(ruta_respaldo)
            logger.info(f"Respaldo creado: {ruta_respaldo} ({tamaño} bytes)")
            print(f"✓ Respaldo creado: {ruta_respaldo}\n")
            
            return ruta_respaldo
        
        except Exception as e:
            logger.error(f"Error al crear respaldo: {e}")
            print(f"✗ Error: {e}\n")
            return None
    
    @staticmethod
    def eliminar_respaldos_antiguos(directorio_respaldo, dias=7):
        """
        Elimina respaldos más antiguos que X días
        
        Args:
            directorio_respaldo: Directorio con respaldos
            dias: Antiguedad máxima en días
        """
        print(f"\n=== ELIMINANDO RESPALDOS ANTIGUOS (> {dias} DÍAS) ===\n")
        
        try:
            archivos = GestorArchivos.recorrer_directorio_recursivo(directorio_respaldo)
            eliminados = 0
            
            for archivo_info in archivos:
                antiguedad = GestorArchivos.obtener_antiguedad_dias(archivo_info['ruta'])
                
                if antiguedad and antiguedad > dias:
                    if GestorArchivos.eliminar_archivo(archivo_info['ruta']):
                        eliminados += 1
            
            logger.info(f"Respaldos antiguos eliminados: {eliminados}")
            print(f"✓ {eliminados} respaldos eliminados\n")
        
        except Exception as e:
            logger.error(f"Error al eliminar respaldos: {e}")

# ===== FUNCIONES DE MONITOREO DE SISTEMA =====

class MonitorSistema:
    """Monitorea recursos del sistema"""
    
    @staticmethod
    def obtener_uso_cpu(intervalo=1):
        """Obtiene porcentaje de uso de CPU"""
        return psutil.cpu_percent(interval=intervalo)
    
    @staticmethod
    def obtener_uso_memoria():
        """Obtiene información de memoria"""
        memoria = psutil.virtual_memory()
        return {
            'total': memoria.total / (1024 ** 3),  # GB
            'usado': memoria.used / (1024 ** 3),
            'disponible': memoria.available / (1024 ** 3),
            'porcentaje': memoria.percent
        }
    
    @staticmethod
    def obtener_uso_disco():
        """Obtiene información de disco"""
        disco = shutil.disk_usage('/')
        return {
            'total': disco.total / (1024 ** 3),  # GB
            'usado': disco.used / (1024 ** 3),
            'libre': disco.free / (1024 ** 3),
            'porcentaje': (disco.used / disco.total) * 100
        }
    
    @staticmethod
    def obtener_procesos_activos():
        """Obtiene número de procesos activos"""
        return len(psutil.pids())
    
    @staticmethod
    def mostrar_reporte_sistema():
        """Muestra reporte completo del sistema"""
        print("\n" + "="*60)
        print("REPORTE DEL SISTEMA")
        print("="*60)
        
        # CPU
        print("\n📊 CPU:")
        cpu_percent = MonitorSistema.obtener_uso_cpu()
        print(f"  Uso: {cpu_percent}%")
        print(f"  Núcleos: {psutil.cpu_count()}")
        
        # Memoria
        print("\n💾 MEMORIA:")
        memoria = MonitorSistema.obtener_uso_memoria()
        print(f"  Total: {memoria['total']:.2f} GB")
        print(f"  Usado: {memoria['usado']:.2f} GB ({memoria['porcentaje']}%)")
        print(f"  Disponible: {memoria['disponible']:.2f} GB")
        
        # Disco
        print("\n💿 DISCO:")
        disco = MonitorSistema.obtener_uso_disco()
        print(f"  Total: {disco['total']:.2f} GB")
        print(f"  Usado: {disco['usado']:.2f} GB ({disco['porcentaje']:.2f}%)")
        print(f"  Libre: {disco['libre']:.2f} GB")
        
        # Procesos
        print("\n⚙️  PROCESOS:")
        print(f"  Activos: {MonitorSistema.obtener_procesos_activos()}")
        
        print("\n" + "="*60 + "\n")

# ===== FUNCIONES DE REPORTES =====

class GeneradorReportes:
    """Genera reportes automáticos"""
    
    @staticmethod
    def generar_reporte_actividad(directorio_monitoreo):
        """Genera reporte de actividad de archivos"""
        print(f"\n=== GENERANDO REPORTE DE ACTIVIDAD ===\n")
        
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            nombre_reporte = f"reporte_actividad_{timestamp}.json"
            ruta_reporte = os.path.join(DIRECTORIO_REPORTES, nombre_reporte)
            
            archivos = GestorArchivos.recorrer_directorio_recursivo(directorio_monitoreo)
            
            reporte = {
                'fecha_generacion': datetime.now().isoformat(),
                'directorio_monitoreado': directorio_monitoreo,
                'total_archivos': len(archivos),
                'tamaño_total_mb': sum(a['tamaño'] for a in archivos) / (1024 * 1024),
                'archivos': []
            }
            
            # Agregar detalles de archivos
            for archivo in archivos:
                reporte['archivos'].append({
                    'nombre': archivo['nombre'],
                    'ruta': archivo['ruta'],
                    'tamaño_kb': archivo['tamaño'] / 1024,
                    'modificado': archivo['modificado'].isoformat() if archivo['modificado'] else None
                })
            
            # Guardar reporte
            with open(ruta_reporte, 'w', encoding='utf-8') as f:
                json.dump(reporte, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Reporte generado: {ruta_reporte}")
            print(f"✓ Reporte generado: {nombre_reporte}")
            print(f"  Total archivos: {reporte['total_archivos']}")
            print(f"  Tamaño total: {reporte['tamaño_total_mb']:.2f} MB\n")
            
            return ruta_reporte
        
        except Exception as e:
            logger.error(f"Error al generar reporte: {e}")
            print(f"✗ Error: {e}\n")
            return None
    
    @staticmethod
    def generar_reporte_sistema():
        """Genera reporte del sistema y lo guarda"""
        print(f"\n=== GENERANDO REPORTE DEL SISTEMA ===\n")
        
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            nombre_reporte = f"reporte_sistema_{timestamp}.json"
            ruta_reporte = os.path.join(DIRECTORIO_REPORTES, nombre_reporte)
            
            reporte = {
                'fecha_generacion': datetime.now().isoformat(),
                'cpu': {
                    'uso_porcentaje': MonitorSistema.obtener_uso_cpu(),
                    'nucleos': psutil.cpu_count()
                },
                'memoria': MonitorSistema.obtener_uso_memoria(),
                'disco': MonitorSistema.obtener_uso_disco(),
                'procesos': MonitorSistema.obtener_procesos_activos()
            }
            
            with open(ruta_reporte, 'w') as f:
                json.dump(reporte, f, indent=2)
            
            logger.info(f"Reporte del sistema generado: {ruta_reporte}")
            print(f"✓ Reporte del sistema guardado\n")
            
            return ruta_reporte
        
        except Exception as e:
            logger.error(f"Error al generar reporte del sistema: {e}")
            print(f"✗ Error: {e}\n")
            return None

# ===== FUNCIONES DE EMAIL (OPCIONAL) =====

class NotificadorEmail:
    """Envía notificaciones por email"""
    
    @staticmethod
    def enviar_email(remitente, contraseña, destinatario, asunto, cuerpo):
        """
        Envía un email
        
        Args:
            remitente: Email del remitente
            contraseña: Contraseña/token de aplicación
            destinatario: Email del destinatario
            asunto: Asunto del email
            cuerpo: Cuerpo del email
        """
        try:
            # Crear mensaje
            mensaje = MIMEMultipart()
            mensaje['From'] = remitente
            mensaje['To'] = destinatario
            mensaje['Subject'] = asunto
            
            mensaje.attach(MIMEText(cuerpo, 'plain'))
            
            # Enviar (Gmail example - requiere contraseña de aplicación)
            # servidor = smtplib.SMTP('smtp.gmail.com', 587)
            # servidor.starttls()
            # servidor.login(remitente, contraseña)
            # servidor.send_message(mensaje)
            # servidor.quit()
            
            logger.info(f"Email enviado a {destinatario}")
            print(f"✓ Email enviado a {destinatario}")
            return True
        
        except Exception as e:
            logger.error(f"Error al enviar email: {e}")
            print(f"✗ Error: {e}")
            return False

# ===== FUNCIONES DE PROGRAMACIÓN DE TAREAS =====

class ProgramadorTareas:
    """Programa tareas automáticas"""
    
    @staticmethod
    def programar_tareas():
        """Programa las tareas automáticas"""
        
        print("\n=== PROGRAMANDO TAREAS AUTOMÁTICAS ===\n")
        
        # Tareas diarias
        schedule.every().day.at("09:00").do(GestorRespaldos.crear_respaldo, 
                                            DIRECTORIO_MONITOREO, DIRECTORIO_RESPALDO)
        print("✓ Respaldo diario a las 09:00")
        
        schedule.every().day.at("20:00").do(LimpiadorArchivos.limpiar_archivos_antiguos,
                                            DIRECTORIO_MONITOREO)
        print("✓ Limpieza diaria a las 20:00")
        
        schedule.every().week.do(GestorRespaldos.eliminar_respaldos_antiguos,
                                DIRECTORIO_RESPALDO)
        print("✓ Eliminación de respaldos antiguos (semanal)")
        
        # Tareas cada hora
        schedule.every().hour.do(MonitorSistema.mostrar_reporte_sistema)
        print("✓ Monitoreo del sistema (cada hora)")
        
        schedule.every().hour.do(GeneradorReportes.generar_reporte_sistema)
        print("✓ Generación de reporte del sistema (cada hora)")
        
        # Tareas cada 30 minutos
        schedule.every(30).minutes.do(GeneradorReportes.generar_reporte_actividad,
                                     DIRECTORIO_MONITOREO)
        print("✓ Generación de reporte de actividad (cada 30 min)")
        
        schedule.every(30).minutes.do(LimpiadorArchivos.limpiar_espacio_disco)
        print("✓ Verificación de espacio en disco (cada 30 min)\n")
    
    @staticmethod
    def ejecutar_programador(modo_demo=False):
        """
        Ejecuta el programador de tareas
        
        Args:
            modo_demo: Si es True, ejecuta una vez y sale
        """
        print("\n" + "="*60)
        print("AUTOMATIZADOR DE TAREAS - EJECUTÁNDOSE")
        print("="*60)
        
        ProgramadorTareas.programar_tareas()
        
        if modo_demo:
            print("\n🚀 Ejecutando tareas en modo DEMOSTRACIÓN...\n")
            # Ejecutar todas las tareas una vez
            schedule.run_all()
            print("\n✓ Demo completada\n")
        else:
            print("\n🚀 Sistema de automatización activo...")
            print("Presiona Ctrl+C para detener\n")
            
            try:
                while True:
                    schedule.run_pending()
                    time.sleep(60)
            
            except KeyboardInterrupt:
                print("\n\n✓ Automatización detenida")

# ===== MENÚ INTERACTIVO =====

def menu_interactivo():
    """Menú interactivo para automatización"""
    
    while True:
        print("\n" + "="*60)
        print("=== AUTOMATIZACIÓN DE TAREAS ===")
        print("="*60)
        print("\n--- GESTIÓN DE ARCHIVOS ---")
        print("1. Crear respaldo manual")
        print("2. Limpiar archivos antiguos")
        print("3. Limpiar archivos temporales")
        print("4. Listar archivos monitoreados")
        print("\n--- MONITOREO ---")
        print("5. Ver reporte del sistema")
        print("6. Generar reporte de actividad")
        print("7. Verificar espacio en disco")
        print("\n--- AUTOMATIZACIÓN ---")
        print("8. Ejecutar automatización (demo)")
        print("9. Programador de tareas (tiempo real)")
        print("\n10. Salir")
        print("="*60)
        
        opcion = input("\nElige una opción (1-10): ").strip()
        
        try:
            # Asegurarse de que existen directorios
            GestorArchivos.crear_directorio(DIRECTORIO_MONITOREO)
            GestorArchivos.crear_directorio(DIRECTORIO_RESPALDO)
            GestorArchivos.crear_directorio(DIRECTORIO_TEMP)
            GestorArchivos.crear_directorio(DIRECTORIO_REPORTES)
            
            if opcion == "1":
                GestorRespaldos.crear_respaldo(DIRECTORIO_MONITOREO, DIRECTORIO_RESPALDO)
            
            elif opcion == "2":
                dias = int(input("Días de antiguedad (default 30): ") or "30")
                LimpiadorArchivos.limpiar_archivos_antiguos(DIRECTORIO_MONITOREO, dias)
            
            elif opcion == "3":
                LimpiadorArchivos.limpiar_archivos_temporales()
            
            elif opcion == "4":
                print("\n=== ARCHIVOS MONITOREADOS ===\n")
                archivos = GestorArchivos.recorrer_directorio_recursivo(DIRECTORIO_MONITOREO)
                if archivos:
                    print(f"Total: {len(archivos)} archivos\n")
                    for archivo in archivos[:10]:  # Mostrar primeros 10
                        tamaño_kb = archivo['tamaño'] / 1024
                        print(f"  {archivo['nombre']} ({tamaño_kb:.2f} KB)")
                    if len(archivos) > 10:
                        print(f"  ... y {len(archivos) - 10} más")
                else:
                    print("No hay archivos monitoreados\n")
            
            elif opcion == "5":
                MonitorSistema.mostrar_reporte_sistema()
            
            elif opcion == "6":
                GeneradorReportes.generar_reporte_actividad(DIRECTORIO_MONITOREO)
            
            elif opcion == "7":
                print()
                LimpiadorArchivos.limpiar_espacio_disco()
            
            elif opcion == "8":
                ProgramadorTareas.ejecutar_programador(modo_demo=True)
            
            elif opcion == "9":
                ProgramadorTareas.ejecutar_programador(modo_demo=False)
            
            elif opcion == "10":
                print("\n✓ ¡Hasta luego!")
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
    print("SISTEMA DE AUTOMATIZACIÓN DE TAREAS")
    print("="*60)
    
    logger.info("Sistema de automatización iniciado")
    
    # Crear directorios necesarios
    GestorArchivos.crear_directorio(DIRECTORIO_MONITOREO)
    GestorArchivos.crear_directorio(DIRECTORIO_RESPALDO)
    GestorArchivos.crear_directorio(DIRECTORIO_TEMP)
    GestorArchivos.crear_directorio(DIRECTORIO_REPORTES)
    
    # Ejecutar menú
    menu_interactivo()
    
    logger.info("Sistema de automatización finalizado")

# === DESAFÍOS ADICIONALES ===
# 1. Integración con webhooks para notificaciones
# 2. Sincronización con la nube (Google Drive, Dropbox)
# 3. Monitoreo de cambios en directorios en tiempo real
# 4. Generación de reportes HTML interactivos
# 5. Integración con servicios como IFTTT
# 6. Sistema de alertas configurables
# 7. Base de datos de historial de tareas
# 8. API REST para control remoto de automatizaciones
