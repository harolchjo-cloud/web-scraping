# Ejercicio 16: Análisis de Datos con Pandas - Manipulación de DataFrames
# Objetivo: Aprender a cargar, limpiar, transformar y analizar datos con Pandas

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

# ===== CONSTANTES =====

ARCHIVO_VENTAS = "ventas.csv"
ARCHIVO_CLIENTES = "clientes.csv"
ARCHIVO_PRODUCTOS = "productos.csv"

# ===== FUNCIONES PARA GENERAR DATOS DE EJEMPLO =====

def generar_datos_ejemplo():
    """
    Genera archivos CSV de ejemplo para análisis
    """
    print("=== GENERANDO DATOS DE EJEMPLO ===\n")
    
    # Crear datos de productos
    productos_data = {
        'producto_id': range(1, 11),
        'nombre': [
            'Laptop', 'Mouse', 'Teclado', 'Monitor', 'Headphones',
            'Webcam', 'SSD', 'RAM', 'Fuente Power', 'Refrigeración'
        ],
        'categoria': [
            'Electrónica', 'Accesorios', 'Accesorios', 'Electrónica', 'Audio',
            'Accesorios', 'Almacenamiento', 'Memoria', 'Fuentes', 'Enfriamiento'
        ],
        'precio': [899.99, 29.99, 79.99, 299.99, 149.99, 79.99, 129.99, 89.99, 99.99, 59.99],
        'stock': [5, 50, 20, 10, 15, 20, 30, 25, 15, 40]
    }
    
    df_productos = pd.DataFrame(productos_data)
    df_productos.to_csv(ARCHIVO_PRODUCTOS, index=False, encoding='utf-8')
    print(f"✓ Archivo '{ARCHIVO_PRODUCTOS}' creado ({len(df_productos)} productos)")
    
    # Crear datos de clientes
    clientes_data = {
        'cliente_id': range(1, 21),
        'nombre': [
            'Juan García', 'María López', 'Carlos Rodríguez', 'Ana Martínez', 'Pedro Sánchez',
            'Laura Giménez', 'Diego Torres', 'Isabel Ruiz', 'Miguel Fernández', 'Rosa García',
            'Antonio López', 'Carmen Rodríguez', 'Francisco Martínez', 'Dolores Sánchez', 'José García',
            'Francisca López', 'Manuel Rodríguez', 'Josefa Martínez', 'Juan Luis Sánchez', 'María del Carmen García'
        ],
        'ciudad': [
            'Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao',
            'Palma', 'Madrid', 'Barcelona', 'Valencia', 'Madrid',
            'Sevilla', 'Bilbao', 'Madrid', 'Barcelona', 'Valencia',
            'Sevilla', 'Madrid', 'Barcelona', 'Valencia', 'Madrid'
        ],
        'pais': ['España'] * 20,
        'fecha_registro': pd.date_range('2023-01-01', periods=20, freq='W').tolist()
    }
    
    df_clientes = pd.DataFrame(clientes_data)
    df_clientes.to_csv(ARCHIVO_CLIENTES, index=False, encoding='utf-8')
    print(f"✓ Archivo '{ARCHIVO_CLIENTES}' creado ({len(df_clientes)} clientes)")
    
    # Crear datos de ventas
    np.random.seed(42)
    ventas_data = {
        'venta_id': range(1, 101),
        'cliente_id': np.random.randint(1, 21, 100),
        'producto_id': np.random.randint(1, 11, 100),
        'cantidad': np.random.randint(1, 5, 100),
        'fecha': pd.date_range('2024-01-01', periods=100, freq='D').tolist(),
        'descuento': np.random.choice([0, 5, 10, 15, 20], 100),
    }
    
    df_ventas = pd.DataFrame(ventas_data)
    df_ventas.to_csv(ARCHIVO_VENTAS, index=False, encoding='utf-8')
    print(f"✓ Archivo '{ARCHIVO_VENTAS}' creado ({len(df_ventas)} ventas)\n")
    
    return df_productos, df_clientes, df_ventas

# ===== FUNCIONES DE CARGA Y EXPLORACIÓN =====

def cargar_datos():
    """
    Carga todos los archivos CSV
    """
    print("=== CARGANDO DATOS ===\n")
    
    try:
        df_productos = pd.read_csv(ARCHIVO_PRODUCTOS)
        df_clientes = pd.read_csv(ARCHIVO_CLIENTES)
        df_ventas = pd.read_csv(ARCHIVO_VENTAS)
        
        # Convertir fechas
        df_clientes['fecha_registro'] = pd.to_datetime(df_clientes['fecha_registro'])
        df_ventas['fecha'] = pd.to_datetime(df_ventas['fecha'])
        
        print("✓ Datos cargados exitosamente\n")
        return df_productos, df_clientes, df_ventas
    
    except FileNotFoundError:
        print("⚠ Archivos no encontrados. Generando datos de ejemplo...\n")
        return generar_datos_ejemplo()

def explorar_dataframe(df, nombre):
    """
    Muestra información general de un DataFrame
    """
    print(f"\n=== EXPLORACIÓN DE {nombre.upper()} ===\n")
    
    print(f"Dimensiones: {df.shape[0]} filas × {df.shape[1]} columnas")
    print(f"\nPrimeras 5 filas:")
    print(df.head())
    
    print(f"\nTipos de datos:")
    print(df.dtypes)
    
    print(f"\nEstadísticas descriptivas:")
    print(df.describe())
    
    print(f"\nValores nulos:")
    print(df.isnull().sum())
    
    print(f"\nInformación general:")
    print(df.info())

# ===== OPERACIONES BÁSICAS =====

def operaciones_basicas(df_productos, df_ventas):
    """
    Demuestra operaciones básicas con DataFrames
    """
    print("\n" + "="*60)
    print("OPERACIONES BÁSICAS")
    print("="*60)
    
    # 1. Selección de columnas
    print("\n1. SELECCIÓN DE COLUMNAS")
    print("Una sola columna (Series):")
    print(df_productos['nombre'].head())
    
    print("\nVarias columnas (DataFrame):")
    print(df_productos[['nombre', 'precio']].head())
    
    # 2. Filtrado
    print("\n2. FILTRADO DE DATOS")
    print("Productos con precio > $100:")
    caros = df_productos[df_productos['precio'] > 100]
    print(caros[['nombre', 'precio']])
    
    # 3. Ordenamiento
    print("\n3. ORDENAMIENTO")
    print("Productos ordenados por precio (descendente):")
    print(df_productos.sort_values('precio', ascending=False)[['nombre', 'precio']])
    
    # 4. Nuevas columnas
    print("\n4. CREAR NUEVAS COLUMNAS")
    df_productos['precio_con_iva'] = df_productos['precio'] * 1.21
    print(df_productos[['nombre', 'precio', 'precio_con_iva']].head())
    
    # 5. Agregar columna en ventas (precio unitario)
    print("\n5. UNIÓN DE DATOS (MERGE)")
    df_ventas_completo = pd.merge(
        df_ventas,
        df_productos[['producto_id', 'nombre', 'precio']],
        on='producto_id'
    )
    df_ventas_completo['total'] = df_ventas_completo['cantidad'] * df_ventas_completo['precio']
    df_ventas_completo['total_con_descuento'] = df_ventas_completo['total'] * (1 - df_ventas_completo['descuento'] / 100)
    
    print(df_ventas_completo[['venta_id', 'nombre', 'cantidad', 'total', 'descuento', 'total_con_descuento']].head())
    
    return df_ventas_completo

# ===== LIMPIEZA DE DATOS =====

def limpieza_datos(df):
    """
    Demuestra técnicas de limpieza de datos
    """
    print("\n" + "="*60)
    print("LIMPIEZA DE DATOS")
    print("="*60)
    
    # Crear DataFrame con datos sucios
    datos_sucios = {
        'id': [1, 2, 3, 4, 5, 6, 7, 8],
        'nombre': ['Juan', 'María', 'Juan', 'Pedro', 'María', 'Juan', 'Ana', 'Juan'],
        'edad': [25, 30, 25, None, 35, 25, 28, 32],
        'salario': [2000, 2500, 2000, 3000, 2500, 2000, 2200, 3000]
    }
    df_sucio = pd.DataFrame(datos_sucios)
    
    print("\n1. DATOS ORIGINALES")
    print(df_sucio)
    print(f"\nValores nulos: {df_sucio.isnull().sum().sum()}")
    
    # Eliminar nulos
    print("\n2. ELIMINAR FILAS CON NULOS")
    df_sin_nulos = df_sucio.dropna()
    print(df_sin_nulos)
    
    # Rellenar nulos
    print("\n3. RELLENAR NULOS")
    df_rellenado = df_sucio.fillna(df_sucio['edad'].mean())
    print(df_rellenado)
    
    # Eliminar duplicados
    print("\n4. ELIMINAR DUPLICADOS")
    df_sin_duplicados = df_sucio.drop_duplicates()
    print(f"Filas antes: {len(df_sucio)}, Filas después: {len(df_sin_duplicados)}")
    print(df_sin_duplicados)
    
    # Reemplazar valores
    print("\n5. REEMPLAZAR VALORES")
    df_reemplazado = df_sucio.replace({'Juan': 'John', 'María': 'Mary'})
    print(df_reemplazado[['nombre']])

# ===== AGRUPACIÓN Y AGREGACIÓN =====

def agrupacion_datos(df_ventas_completo, df_clientes):
    """
    Demuestra agrupación y agregación
    """
    print("\n" + "="*60)
    print("AGRUPACIÓN Y AGREGACIÓN")
    print("="*60)
    
    # 1. Suma por producto
    print("\n1. VENTAS TOTALES POR PRODUCTO")
    ventas_por_producto = df_ventas_completo.groupby('nombre').agg({
        'cantidad': 'sum',
        'total_con_descuento': 'sum',
        'venta_id': 'count'
    }).rename(columns={'venta_id': 'num_ventas'}).sort_values('total_con_descuento', ascending=False)
    print(ventas_por_producto)
    
    # 2. Ventas por cliente
    print("\n2. GASTO TOTAL POR CLIENTE")
    df_ventas_con_cliente = pd.merge(
        df_ventas_completo,
        df_clientes[['cliente_id', 'nombre']],
        left_on='cliente_id',
        right_on='cliente_id',
        suffixes=('_producto', '_cliente')
    )
    
    ventas_por_cliente = df_ventas_con_cliente.groupby('nombre_cliente').agg({
        'total_con_descuento': 'sum',
        'venta_id': 'count'
    }).rename(columns={'venta_id': 'num_compras'}).sort_values('total_con_descuento', ascending=False).head(10)
    print(ventas_por_cliente)
    
    # 3. Ventas por ciudad
    print("\n3. VENTAS TOTALES POR CIUDAD")
    df_ventas_ciudad = pd.merge(
        df_ventas_completo,
        df_clientes[['cliente_id', 'ciudad']],
        on='cliente_id'
    )
    
    ventas_por_ciudad = df_ventas_ciudad.groupby('ciudad').agg({
        'total_con_descuento': 'sum',
        'venta_id': 'count',
        'cliente_id': 'nunique'
    }).rename(columns={
        'venta_id': 'num_transacciones',
        'cliente_id': 'num_clientes',
        'total_con_descuento': 'ingresos'
    }).sort_values('ingresos', ascending=False)
    print(ventas_por_ciudad)
    
    # 4. Estadísticas por rango de fechas
    print("\n4. VENTAS POR SEMANA")
    df_ventas_completo['semana'] = df_ventas_completo['fecha'].dt.isocalendar().week
    ventas_por_semana = df_ventas_completo.groupby('semana').agg({
        'total_con_descuento': 'sum',
        'venta_id': 'count'
    }).rename(columns={'venta_id': 'num_ventas'})
    print(ventas_por_semana.head())

# ===== ANÁLISIS ESTADÍSTICO =====

def analisis_estadistico(df_ventas_completo):
    """
    Demuestra análisis estadísticos
    """
    print("\n" + "="*60)
    print("ANÁLISIS ESTADÍSTICO")
    print("="*60)
    
    # Estadísticas básicas
    print("\n1. ESTADÍSTICAS BÁSICAS")
    print(f"Venta promedio: ${df_ventas_completo['total_con_descuento'].mean():.2f}")
    print(f"Venta mediana: ${df_ventas_completo['total_con_descuento'].median():.2f}")
    print(f"Venta mínima: ${df_ventas_completo['total_con_descuento'].min():.2f}")
    print(f"Venta máxima: ${df_ventas_completo['total_con_descuento'].max():.2f}")
    print(f"Desviación estándar: ${df_ventas_completo['total_con_descuento'].std():.2f}")
    
    # Distribución de valores
    print("\n2. DISTRIBUCIÓN DE DESCUENTOS")
    print(df_ventas_completo['descuento'].value_counts().sort_index())
    
    # Percentiles
    print("\n3. PERCENTILES DE VENTA")
    percentiles = df_ventas_completo['total_con_descuento'].quantile([0.25, 0.5, 0.75, 0.9, 0.95])
    for pct, valor in percentiles.items():
        print(f"P{int(pct*100)}: ${valor:.2f}")
    
    # Correlación
    print("\n4. MATRIZ DE CORRELACIÓN")
    df_num = df_ventas_completo[['cantidad', 'descuento', 'total']].corr()
    print(df_num)

# ===== TRANSFORMACIONES Y OPERACIONES ESPECIALES =====

def transformaciones_especiales(df_productos, df_ventas_completo):
    """
    Demuestra transformaciones y operaciones especiales
    """
    print("\n" + "="*60)
    print("TRANSFORMACIONES Y OPERACIONES ESPECIALES")
    print("="*60)
    
    # 1. Map
    print("\n1. FUNCIÓN MAP")
    categoria_map = {
        'Electrónica': 'Premium',
        'Accesorios': 'Accesorios',
        'Almacenamiento': 'Premium',
        'Memoria': 'Premium',
        'Fuentes': 'Componentes',
        'Enfriamiento': 'Componentes',
        'Audio': 'Accesorios'
    }
    df_productos['tipo'] = df_productos['categoria'].map(categoria_map)
    print(df_productos[['nombre', 'categoria', 'tipo']].head())
    
    # 2. Apply
    print("\n2. FUNCIÓN APPLY")
    def clasificar_cantidad(cantidad):
        if cantidad >= 3:
            return 'Alto'
        elif cantidad == 2:
            return 'Medio'
        else:
            return 'Bajo'
    
    df_ventas_completo['volumen'] = df_ventas_completo['cantidad'].apply(clasificar_cantidad)
    print(df_ventas_completo[['venta_id', 'cantidad', 'volumen']].head(10))
    
    # 3. Pivot Table
    print("\n3. PIVOT TABLE")
    pivot = df_ventas_completo.pivot_table(
        values='total_con_descuento',
        index='nombre',
        columns='descuento',
        aggfunc='sum',
        fill_value=0
    )
    print(pivot.head())
    
    # 4. Función lambda
    print("\n4. FUNCIÓN LAMBDA")
    df_ventas_completo['beneficio_estimado'] = df_ventas_completo['total_con_descuento'].apply(
        lambda x: x * 0.30 if x > 200 else x * 0.25
    )
    print(df_ventas_completo[['venta_id', 'total_con_descuento', 'beneficio_estimado']].head())

# ===== EXPORTACIÓN =====

def exportar_datos(df_productos, df_ventas_completo):
    """
    Demuestra exportación a diferentes formatos
    """
    print("\n" + "="*60)
    print("EXPORTACIÓN DE DATOS")
    print("="*60)
    
    # Exportar a CSV
    df_productos.to_csv('productos_procesados.csv', index=False, encoding='utf-8')
    print("\n✓ Exportado: productos_procesados.csv")
    
    # Exportar a Excel (si está disponible)
    try:
        df_productos.to_excel('productos_procesados.xlsx', index=False)
        print("✓ Exportado: productos_procesados.xlsx")
    except:
        print("⚠ openpyxl no instalado para exportar a Excel")
    
    # Exportar a JSON
    df_ventas_completo.head(10).to_json('ventas_muestra.json', orient='records', indent=2)
    print("✓ Exportado: ventas_muestra.json")
    
    # Exportar a HTML
    df_productos.head(10).to_html('productos_tabla.html', index=False)
    print("✓ Exportado: productos_tabla.html")

# ===== MENÚ INTERACTIVO =====

def menu_interactivo(df_productos, df_clientes, df_ventas):
    """
    Menú interactivo para explorar datos
    """
    
    while True:
        print("\n" + "="*60)
        print("=== ANÁLISIS DE DATOS CON PANDAS ===")
        print("="*60)
        print("1. Explorar DataFrames")
        print("2. Operaciones básicas")
        print("3. Limpieza de datos (demostración)")
        print("4. Agrupación y agregación")
        print("5. Análisis estadístico")
        print("6. Transformaciones especiales")
        print("7. Exportar datos")
        print("8. Búsqueda personalizada")
        print("9. Salir")
        print("="*60)
        
        opcion = input("\nElige una opción (1-9): ").strip()
        
        try:
            if opcion == "1":
                explorar_dataframe(df_productos, "Productos")
                explorar_dataframe(df_clientes, "Clientes")
                explorar_dataframe(df_ventas, "Ventas")
            
            elif opcion == "2":
                df_ventas_completo = operaciones_basicas(df_productos.copy(), df_ventas.copy())
            
            elif opcion == "3":
                limpieza_datos(df_productos)
            
            elif opcion == "4":
                df_ventas_completo = pd.merge(
                    df_ventas,
                    df_productos[['producto_id', 'nombre', 'precio']],
                    on='producto_id'
                )
                df_ventas_completo['total'] = df_ventas_completo['cantidad'] * df_ventas_completo['precio']
                df_ventas_completo['total_con_descuento'] = df_ventas_completo['total'] * (1 - df_ventas_completo['descuento'] / 100)
                agrupacion_datos(df_ventas_completo, df_clientes)
            
            elif opcion == "5":
                df_ventas_completo = pd.merge(
                    df_ventas,
                    df_productos[['producto_id', 'nombre', 'precio']],
                    on='producto_id'
                )
                df_ventas_completo['total'] = df_ventas_completo['cantidad'] * df_ventas_completo['precio']
                df_ventas_completo['total_con_descuento'] = df_ventas_completo['total'] * (1 - df_ventas_completo['descuento'] / 100)
                analisis_estadistico(df_ventas_completo)
            
            elif opcion == "6":
                df_ventas_completo = pd.merge(
                    df_ventas,
                    df_productos[['producto_id', 'nombre', 'precio']],
                    on='producto_id'
                )
                df_ventas_completo['total'] = df_ventas_completo['cantidad'] * df_ventas_completo['precio']
                df_ventas_completo['total_con_descuento'] = df_ventas_completo['total'] * (1 - df_ventas_completo['descuento'] / 100)
                transformaciones_especiales(df_productos.copy(), df_ventas_completo)
            
            elif opcion == "7":
                df_ventas_completo = pd.merge(
                    df_ventas,
                    df_productos[['producto_id', 'nombre', 'precio']],
                    on='producto_id'
                )
                df_ventas_completo['total'] = df_ventas_completo['cantidad'] * df_ventas_completo['precio']
                df_ventas_completo['total_con_descuento'] = df_ventas_completo['total'] * (1 - df_ventas_completo['descuento'] / 100)
                exportar_datos(df_productos, df_ventas_completo)
            
            elif opcion == "8":
                print("\n=== BÚSQUEDA PERSONALIZADA ===")
                print("1. Buscar producto por nombre")
                print("2. Filtrar por precio")
                print("3. Filtrar por stock")
                print("4. Buscar cliente por ciudad")
                
                sub_opcion = input("Elige una opción (1-4): ").strip()
                
                if sub_opcion == "1":
                    nombre = input("Nombre o parte del nombre: ").lower()
                    resultados = df_productos[df_productos['nombre'].str.lower().str.contains(nombre)]
                    print("\nResultados:")
                    print(resultados[['nombre', 'precio', 'stock']])
                
                elif sub_opcion == "2":
                    min_precio = float(input("Precio mínimo: $"))
                    max_precio = float(input("Precio máximo: $"))
                    resultados = df_productos[(df_productos['precio'] >= min_precio) & (df_productos['precio'] <= max_precio)]
                    print("\nProductos en rango:")
                    print(resultados[['nombre', 'precio', 'stock']])
                
                elif sub_opcion == "3":
                    min_stock = int(input("Stock mínimo: "))
                    resultados = df_productos[df_productos['stock'] >= min_stock]
                    print(f"\nProductos con stock >= {min_stock}:")
                    print(resultados[['nombre', 'stock']])
                
                elif sub_opcion == "4":
                    ciudad = input("Ciudad: ").lower()
                    resultados = df_clientes[df_clientes['ciudad'].str.lower().str.contains(ciudad)]
                    print(f"\nClientes en {ciudad}:")
                    print(resultados[['nombre', 'ciudad']])
            
            elif opcion == "9":
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
    print("ANÁLISIS DE DATOS CON PANDAS")
    print("="*60)
    
    # Cargar o generar datos
    df_productos, df_clientes, df_ventas = cargar_datos()
    
    # Ejecutar menú interactivo
    menu_interactivo(df_productos, df_clientes, df_ventas)

# === DESAFÍOS ADICIONALES ===
# 1. Crear visualizaciones con matplotlib
# 2. Importar datos de APIs REST
# 3. Implementar predicción con Machine Learning
# 4. Crear dashboard interactivo con Plotly
# 5. Procesamiento de datos en tiempo real
# 6. Análisis de series temporales
# 7. Integración con bases de datos SQL
