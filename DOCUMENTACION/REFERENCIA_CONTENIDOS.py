#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARCHIVO DE REFERENCIA: Contenido de cada módulo del Ejercicio 19
Este archivo documenta exactamente qué contiene cada módulo
"""

CONTENIDO = {
    "ejercicio19.py": {
        "descripcion": "Sistema Básico Completo de Web Scraping",
        "lineas": "~400",
        "tamaño": "16.51 KB",
        "duracion": "15-20 minutos",
        "clases": [
            {
                "nombre": "WebScraper",
                "metodos": [
                    "init(delay)",
                    "descargar_pagina(url)",
                    "extraer_noticias_ejemplo()",
                    "extraer_precios_ejemplo()",
                    "extraer_tabla_html()",
                    "extraer_con_selectores_css()",
                    "guardar_csv(datos, archivo)",
                    "guardar_json(datos, archivo)"
                ]
            }
        ],
        "funciones": [
            "ejemplo_analisis_datos()",
            "ejemplo_expresiones_regulares()",
            "main()"
        ],
        "archivos_generados": [
            "noticias.csv",
            "noticias.json",
            "productos.csv",
            "productos.json",
            "tabla_datos.csv",
            "tabla_datos.json",
            "selectores_css.json"
        ],
        "conceptos": [
            "Descargar páginas web",
            "Parsear HTML con BeautifulSoup",
            "Selectores CSS básicos y avanzados",
            "Expresiones regulares",
            "Análisis con Pandas",
            "Exportación a CSV/JSON",
            "Logging y debugging"
        ],
        "como_ejecutar": "python ejercicio19.py"
    },
    
    "ejercicio19b.py": {
        "descripcion": "Sistema Avanzado con Selenium y Patrones",
        "lineas": "~350",
        "tamaño": "14.31 KB",
        "duracion": "15-20 minutos",
        "clases": [
            {
                "nombre": "ScraperSelenium",
                "metodos": [
                    "init()",
                    "inicializar_driver()",
                    "cerrar_driver()",
                    "esperar_elemento(selector, timeout)",
                    "simular_ejemplo_dinamico()"
                ]
            },
            {
                "nombre": "PatronesAvanzados",
                "metodos_staticos": [
                    "ejemplo_paginacion()",
                    "ejemplo_autenticacion()",
                    "ejemplo_manejo_errores()",
                    "ejemplo_multithreading()",
                    "ejemplo_cache()"
                ]
            },
            {
                "nombre": "MejoresPracticas",
                "metodos_staticos": [
                    "mostrar_guia()"
                ]
            }
        ],
        "funciones": [
            "main()"
        ],
        "conceptos": [
            "Selenium WebDriver",
            "JavaScript y contenido dinámico",
            "WebDriverWait y expected_conditions",
            "Paginación con loops",
            "Autenticación y sesiones",
            "Manejo robusto de errores",
            "Multi-threading",
            "Cacheo de datos",
            "Mejores prácticas",
            "Consideraciones legales"
        ],
        "como_ejecutar": "python ejercicio19b.py",
        "prerequisitos": "ChromeDriver (opcional)"
    },
    
    "ejercicio19c.py": {
        "descripcion": "Ejemplos Prácticos Reutilizables",
        "lineas": "~400",
        "tamaño": "16.6 KB",
        "duracion": "15-20 minutos",
        "clases": [
            {
                "nombre": "ScraperBasico",
                "metodos": [
                    "init(delay)",
                    "obtener(url, max_reintentos)"
                ],
                "features": "Reintentos automáticos, backoff exponencial"
            },
            {
                "nombre": "ExtractorTabla",
                "metodos_staticos": [
                    "html_a_lista_diccionarios(html_tabla)",
                    "guardar_csv(datos, archivo)",
                    "guardar_json(datos, archivo)"
                ]
            },
            {
                "nombre": "ExtractorProducto",
                "metodos_staticos": [
                    "extraer_precio(texto_precio)",
                    "extraer_puntuacion(texto_puntuacion)",
                    "scraping_productos_ejemplo()"
                ]
            },
            {
                "nombre": "MonitorCambios",
                "metodos": [
                    "init(url, archivo_estado)",
                    "cargar_estado()",
                    "guardar_estado(datos)",
                    "detectar_cambios(datos_nuevos)"
                ]
            },
            {
                "nombre": "ExportadorDatos",
                "metodos_staticos": [
                    "a_csv(datos, archivo)",
                    "a_json(datos, archivo)",
                    "a_html(datos, archivo, titulo)"
                ]
            },
            {
                "nombre": "LimpiadorDatos",
                "metodos_staticos": [
                    "limpiar_texto(texto)",
                    "validar_email(email)",
                    "validar_url(url)",
                    "procesar_datos(datos)"
                ]
            },
            {
                "nombre": "LoggerScraping",
                "metodos": [
                    "init(archivo_log)",
                    "registrar(evento, detalles)",
                    "cerrar()"
                ]
            },
            {
                "nombre": "PipelineCompleto",
                "metodos": [
                    "init()",
                    "ejecutar(url, selectores, nombre_archivo)"
                ],
                "features": "Descarga → Parsea → Limpia → Guarda"
            }
        ],
        "funciones": [
            "main()"
        ],
        "archivos_generados": [
            "tabla_ejemplo.csv",
            "tabla_ejemplo.json",
            "productos_ejemplo.csv",
            "productos_ejemplo.json",
            "scraping.log"
        ],
        "conceptos": [
            "Clases reutilizables",
            "Pipelines end-to-end",
            "Limpieza de datos",
            "Validación de datos",
            "Logging y trazabilidad",
            "Monitoreo de cambios",
            "Exportación HTML"
        ],
        "como_ejecutar": "python ejercicio19c.py"
    },
    
    "README_WebScraping.md": {
        "tipo": "Documentación Completa",
        "tamaño": "9.74 KB",
        "secciones": 17,
        "contenido": [
            "1. ¿Qué es Web Scraping?",
            "2. ¿Cómo Funciona?",
            "3. Librerías Principales",
            "4. Archivos Incluidos",
            "5. Instalación y Uso",
            "6. Ejemplos de Código (10+)",
            "7. Selectores CSS - Referencia Rápida",
            "8. Buenas Prácticas",
            "9. Consideraciones Legales",
            "10. Expresiones Regulares",
            "11. Análisis con Pandas",
            "12. Selenium para Dinámicos",
            "13. Patrones Avanzados",
            "14. Comparativa de Herramientas",
            "15. Troubleshooting",
            "16. Recursos Útiles",
            "17. Checklist Final"
        ],
        "mejor_para": "Referencia completa y detallada"
    },
    
    "GUIA_RAPIDA_WebScraping.md": {
        "tipo": "Cheat Sheet Rápido",
        "tamaño": "7.69 KB",
        "secciones": 12,
        "contenido": [
            "1. Inicio Rápido",
            "2. Selectores CSS - Cheat Sheet (15 ejemplos)",
            "3. Patrones Comunes (8 patrones)",
            "4. Limpieza de Datos",
            "5. Análisis con Pandas",
            "6. Selenium",
            "7. Buenas Prácticas (tabla)",
            "8. Troubleshooting",
            "9. Recursos",
            "10. Ejemplo Completo",
            "11. Checklist Pre-scraping",
            "12. Consejos Finales"
        ],
        "mejor_para": "Consulta rápida durante desarrollo"
    },
    
    "RESUMEN_Ejercicio19.md": {
        "tipo": "Resumen Ejecutivo",
        "tamaño": "9.21 KB",
        "secciones": 14,
        "contenido": [
            "1. Archivos Generados (estructura árbol)",
            "2. Lo que Aprendiste (5 categorías)",
            "3. Características Principales",
            "4. Datos Extraídos de Ejemplo",
            "5. Cómo Usar",
            "6. Ejemplos Rápidos",
            "7. Seguridad y Ética",
            "8. Complejidad y Características",
            "9. Conceptos Clave",
            "10. Librerías Utilizadas",
            "11. Próximos Pasos",
            "12. Advertencias",
            "13. Resumen Ejecutivo (tabla)",
            "14. ¡Ejercicio Completado!"
        ],
        "mejor_para": "Visión general del ejercicio"
    },
    
    "INDICE_COMPLETO.md": {
        "tipo": "Índice y Mapa de Contenidos",
        "tamaño": "12.3 KB",
        "secciones": 18,
        "contenido": [
            "1. Objetivo General",
            "2. Estructura del Proyecto",
            "3. Módulos de Código",
            "4. Documentación",
            "5. Datos Generados",
            "6. Quick Start",
            "7. Conceptos Clave",
            "8. Matriz de Aprendizaje",
            "9. Checklist de Validación",
            "10. Logros Alcanzados",
            "11. Soporte y Referencia",
            "12. Próximas Metas",
            "13. Estadísticas",
            "14. Certificación",
            "15-18. Información adicional"
        ],
        "mejor_para": "Navegación y referencia de todo el proyecto"
    }
}

# Resumen de estadísticas
ESTADISTICAS = {
    "total_archivos": 21,
    "codigo_python": 3,
    "documentacion": 4,
    "datos_csv": 5,
    "datos_json": 6,
    "logs": 1,
    "lineas_codigo": "~1,100",
    "clases_implementadas": 11,
    "metodos_total": 40,
    "ejemplos_incluidos": 20,
    "patrones_demostrados": 12,
    "tamaño_total": "~100 KB",
    "tiempo_estudio": "2-3 horas",
    "nivel": "Intermedio-Avanzado"
}

# Mapeo de archivos a conceptos
CONCEPTO_A_ARCHIVO = {
    "Descargar páginas": ["ejercicio19.py", "ejercicio19c.py"],
    "Parsear HTML": ["ejercicio19.py", "ejercicio19b.py", "ejercicio19c.py"],
    "Selectores CSS": ["ejercicio19.py", "README_WebScraping.md", "GUIA_RAPIDA_WebScraping.md"],
    "Expresiones Regulares": ["ejercicio19.py", "ejercicio19c.py"],
    "Pandas": ["ejercicio19.py", "GUIA_RAPIDA_WebScraping.md"],
    "Selenium": ["ejercicio19b.py", "README_WebScraping.md"],
    "Multi-threading": ["ejercicio19b.py", "ejercicio19c.py"],
    "Cacheo": ["ejercicio19b.py"],
    "Limpieza de datos": ["ejercicio19c.py", "GUIA_RAPIDA_WebScraping.md"],
    "Exportación": ["ejercicio19.py", "ejercicio19c.py"],
    "Buenas prácticas": ["ejercicio19b.py", "README_WebScraping.md", "GUIA_RAPIDA_WebScraping.md"],
    "Consideraciones legales": ["ejercicio19b.py", "README_WebScraping.md"]
}

if __name__ == "__main__":
    print("=" * 70)
    print("REFERENCIA DE CONTENIDOS - EJERCICIO 19: WEB SCRAPING")
    print("=" * 70)
    print()
    
    # Mostrar módulos
    print("📚 MÓDULOS DE CÓDIGO:")
    print("-" * 70)
    for archivo, info in CONTENIDO.items():
        if archivo.endswith('.py'):
            print(f"\n✓ {archivo}")
            print(f"  Descripción: {info['descripcion']}")
            print(f"  Tamaño: {info['tamaño']} | Líneas: {info['lineas']}")
            print(f"  Tiempo: {info['duracion']}")
            print(f"  Clases: {len(info['clases'])}")
            if 'metodos_staticos' in str(info):
                print(f"  Ejecutar: {info['como_ejecutar']}")
    
    print("\n\n📖 DOCUMENTACIÓN:")
    print("-" * 70)
    for archivo, info in CONTENIDO.items():
        if archivo.endswith('.md'):
            print(f"\n✓ {archivo}")
            print(f"  Tipo: {info['tipo']}")
            print(f"  Tamaño: {info['tamaño']}")
            print(f"  Secciones: {info['secciones']}")
            print(f"  Mejor para: {info['mejor_para']}")
    
    print("\n\n📊 ESTADÍSTICAS GENERALES:")
    print("-" * 70)
    for clave, valor in ESTADISTICAS.items():
        print(f"  {clave.replace('_', ' ').title()}: {valor}")
    
    print("\n\n✓ EJERCICIO 19: COMPLETADO CON ÉXITO")
    print("=" * 70)
