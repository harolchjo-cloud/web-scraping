# Ejercicio 15: Bases de Datos con SQLite - Almacenamiento Persistente
# Objetivo: Aprender a crear, consultar y manipular bases de datos SQLite

import sqlite3
from datetime import datetime
from pathlib import Path
import json

# ===== CONSTANTES =====

DB_PATH = "tienda_online.db"
TABLA_CLIENTES = "clientes"
TABLA_PRODUCTOS = "productos"
TABLA_PEDIDOS = "pedidos"
TABLA_DETALLES_PEDIDO = "detalles_pedido"

# ===== CLASE PARA GESTIONAR LA BASE DE DATOS =====

class GestorBaseDatos:
    """
    Clase para manejar todas las operaciones de la base de datos
    """
    
    def __init__(self, nombre_db=DB_PATH):
        """
        Inicializa la conexión a la base de datos
        
        Args:
            nombre_db: Nombre del archivo de base de datos
        """
        self.nombre_db = nombre_db
        self.conexion = None
        self.cursor = None
    
    def conectar(self):
        """
        Establece conexión con la base de datos
        """
        try:
            self.conexion = sqlite3.connect(self.nombre_db)
            # Permite acceso a columnas por nombre
            self.conexion.row_factory = sqlite3.Row
            self.cursor = self.conexion.cursor()
            print(f"✓ Conectado a base de datos: {self.nombre_db}")
            return True
        except sqlite3.Error as e:
            print(f"✗ Error al conectar: {e}")
            return False
    
    def desconectar(self):
        """
        Cierra la conexión con la base de datos
        """
        if self.conexion:
            self.conexion.close()
            print("✓ Desconectado de la base de datos")
    
    def ejecutar(self, sql, parametros=None):
        """
        Ejecuta un comando SQL
        
        Args:
            sql: Comando SQL a ejecutar
            parametros: Parámetros para el comando (tuple o dict)
        
        Returns:
            Resultado del cursor
        """
        try:
            if parametros:
                self.cursor.execute(sql, parametros)
            else:
                self.cursor.execute(sql)
            self.conexion.commit()
            return True
        except sqlite3.Error as e:
            print(f"✗ Error SQL: {e}")
            return False
    
    def ejecutar_varios(self, sql, datos):
        """
        Ejecuta un comando SQL múltiples veces con diferentes parámetros
        
        Args:
            sql: Comando SQL a ejecutar
            datos: Lista de tuplas con parámetros
        """
        try:
            self.cursor.executemany(sql, datos)
            self.conexion.commit()
            print(f"✓ {self.cursor.rowcount} registros insertados")
            return True
        except sqlite3.Error as e:
            print(f"✗ Error: {e}")
            return False
    
    def obtener_uno(self, sql, parametros=None):
        """
        Obtiene un registro
        """
        try:
            if parametros:
                self.cursor.execute(sql, parametros)
            else:
                self.cursor.execute(sql)
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"✗ Error: {e}")
            return None
    
    def obtener_todos(self, sql, parametros=None):
        """
        Obtiene todos los registros
        """
        try:
            if parametros:
                self.cursor.execute(sql, parametros)
            else:
                self.cursor.execute(sql)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"✗ Error: {e}")
            return []
    
    def obtener_ultimo_id(self):
        """
        Retorna el ID del último registro insertado
        """
        return self.cursor.lastrowid
    
    def obtener_filas_afectadas(self):
        """
        Retorna número de filas afectadas por la última operación
        """
        return self.cursor.rowcount
    
    def crear_tablas(self):
        """
        Crea todas las tablas necesarias
        """
        print("\n=== CREANDO TABLAS ===")
        
        # Tabla de clientes
        sql_clientes = f"""
        CREATE TABLE IF NOT EXISTS {TABLA_CLIENTES} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            telefono TEXT,
            direccion TEXT,
            fecha_registro DATE DEFAULT CURRENT_DATE
        )
        """
        
        # Tabla de productos
        sql_productos = f"""
        CREATE TABLE IF NOT EXISTS {TABLA_PRODUCTOS} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL,
            categoria TEXT,
            fecha_creacion DATE DEFAULT CURRENT_DATE
        )
        """
        
        # Tabla de pedidos
        sql_pedidos = f"""
        CREATE TABLE IF NOT EXISTS {TABLA_PEDIDOS} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            fecha_pedido DATE DEFAULT CURRENT_DATE,
            estado TEXT DEFAULT 'Pendiente',
            total REAL DEFAULT 0,
            FOREIGN KEY (cliente_id) REFERENCES {TABLA_CLIENTES}(id)
        )
        """
        
        # Tabla de detalles del pedido
        sql_detalles = f"""
        CREATE TABLE IF NOT EXISTS {TABLA_DETALLES_PEDIDO} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pedido_id INTEGER NOT NULL,
            producto_id INTEGER NOT NULL,
            cantidad INTEGER NOT NULL,
            precio_unitario REAL NOT NULL,
            subtotal REAL,
            FOREIGN KEY (pedido_id) REFERENCES {TABLA_PEDIDOS}(id),
            FOREIGN KEY (producto_id) REFERENCES {TABLA_PRODUCTOS}(id)
        )
        """
        
        tablas = [
            ("Clientes", sql_clientes),
            ("Productos", sql_productos),
            ("Pedidos", sql_pedidos),
            ("Detalles Pedido", sql_detalles)
        ]
        
        for nombre, sql in tablas:
            if self.ejecutar(sql):
                print(f"✓ Tabla '{nombre}' creada/verificada")
            else:
                print(f"✗ Error al crear tabla '{nombre}'")

# ===== OPERACIONES CRUD PARA CLIENTES =====

class GestorClientes:
    """Gestiona operaciones con clientes"""
    
    def __init__(self, gestor_db):
        self.db = gestor_db
    
    def crear(self, nombre, email, telefono=None, direccion=None):
        """Crea un nuevo cliente"""
        sql = f"""
        INSERT INTO {TABLA_CLIENTES} (nombre, email, telefono, direccion)
        VALUES (?, ?, ?, ?)
        """
        if self.db.ejecutar(sql, (nombre, email, telefono, direccion)):
            print(f"✓ Cliente '{nombre}' creado (ID: {self.db.obtener_ultimo_id()})")
            return self.db.obtener_ultimo_id()
        return None
    
    def obtener(self, cliente_id):
        """Obtiene un cliente por ID"""
        sql = f"SELECT * FROM {TABLA_CLIENTES} WHERE id = ?"
        return self.db.obtener_uno(sql, (cliente_id,))
    
    def obtener_todos(self):
        """Obtiene todos los clientes"""
        sql = f"SELECT * FROM {TABLA_CLIENTES} ORDER BY nombre"
        return self.db.obtener_todos(sql)
    
    def actualizar(self, cliente_id, nombre=None, email=None, telefono=None, direccion=None):
        """Actualiza datos de un cliente"""
        campos = []
        valores = []
        
        if nombre:
            campos.append("nombre = ?")
            valores.append(nombre)
        if email:
            campos.append("email = ?")
            valores.append(email)
        if telefono:
            campos.append("telefono = ?")
            valores.append(telefono)
        if direccion:
            campos.append("direccion = ?")
            valores.append(direccion)
        
        if not campos:
            return False
        
        valores.append(cliente_id)
        sql = f"UPDATE {TABLA_CLIENTES} SET {', '.join(campos)} WHERE id = ?"
        return self.db.ejecutar(sql, valores)
    
    def eliminar(self, cliente_id):
        """Elimina un cliente"""
        sql = f"DELETE FROM {TABLA_CLIENTES} WHERE id = ?"
        if self.db.ejecutar(sql, (cliente_id,)):
            print(f"✓ Cliente eliminado (filas afectadas: {self.db.obtener_filas_afectadas()})")
            return True
        return False
    
    def buscar_por_email(self, email):
        """Busca un cliente por email"""
        sql = f"SELECT * FROM {TABLA_CLIENTES} WHERE email = ?"
        return self.db.obtener_uno(sql, (email,))
    
    def contar(self):
        """Cuenta total de clientes"""
        sql = f"SELECT COUNT(*) as total FROM {TABLA_CLIENTES}"
        resultado = self.db.obtener_uno(sql)
        return resultado['total'] if resultado else 0

# ===== OPERACIONES CRUD PARA PRODUCTOS =====

class GestorProductos:
    """Gestiona operaciones con productos"""
    
    def __init__(self, gestor_db):
        self.db = gestor_db
    
    def crear(self, nombre, precio, stock, descripcion=None, categoria=None):
        """Crea un nuevo producto"""
        sql = f"""
        INSERT INTO {TABLA_PRODUCTOS} (nombre, precio, stock, descripcion, categoria)
        VALUES (?, ?, ?, ?, ?)
        """
        if self.db.ejecutar(sql, (nombre, precio, stock, descripcion, categoria)):
            print(f"✓ Producto '{nombre}' creado (ID: {self.db.obtener_ultimo_id()})")
            return self.db.obtener_ultimo_id()
        return None
    
    def obtener(self, producto_id):
        """Obtiene un producto por ID"""
        sql = f"SELECT * FROM {TABLA_PRODUCTOS} WHERE id = ?"
        return self.db.obtener_uno(sql, (producto_id,))
    
    def obtener_todos(self):
        """Obtiene todos los productos"""
        sql = f"SELECT * FROM {TABLA_PRODUCTOS} ORDER BY nombre"
        return self.db.obtener_todos(sql)
    
    def obtener_por_categoria(self, categoria):
        """Obtiene productos de una categoría"""
        sql = f"SELECT * FROM {TABLA_PRODUCTOS} WHERE categoria = ? ORDER BY nombre"
        return self.db.obtener_todos(sql, (categoria,))
    
    def actualizar_stock(self, producto_id, cantidad):
        """Actualiza el stock de un producto"""
        sql = f"UPDATE {TABLA_PRODUCTOS} SET stock = stock + ? WHERE id = ?"
        return self.db.ejecutar(sql, (cantidad, producto_id))
    
    def actualizar_precio(self, producto_id, nuevo_precio):
        """Actualiza el precio de un producto"""
        sql = f"UPDATE {TABLA_PRODUCTOS} SET precio = ? WHERE id = ?"
        return self.db.ejecutar(sql, (nuevo_precio, producto_id))
    
    def eliminar(self, producto_id):
        """Elimina un producto"""
        sql = f"DELETE FROM {TABLA_PRODUCTOS} WHERE id = ?"
        return self.db.ejecutar(sql, (producto_id,))
    
    def productos_bajo_stock(self, limite=10):
        """Obtiene productos con stock bajo"""
        sql = f"SELECT * FROM {TABLA_PRODUCTOS} WHERE stock < ? ORDER BY stock"
        return self.db.obtener_todos(sql, (limite,))
    
    def productos_caros(self, limite_precio):
        """Obtiene productos más caros que un precio"""
        sql = f"SELECT * FROM {TABLA_PRODUCTOS} WHERE precio > ? ORDER BY precio DESC"
        return self.db.obtener_todos(sql, (limite_precio,))
    
    def estadisticas(self):
        """Obtiene estadísticas de productos"""
        sql = f"""
        SELECT 
            COUNT(*) as total,
            AVG(precio) as precio_promedio,
            MIN(precio) as precio_minimo,
            MAX(precio) as precio_maximo,
            SUM(stock) as stock_total
        FROM {TABLA_PRODUCTOS}
        """
        return self.db.obtener_uno(sql)

# ===== OPERACIONES CRUD PARA PEDIDOS =====

class GestorPedidos:
    """Gestiona operaciones con pedidos"""
    
    def __init__(self, gestor_db):
        self.db = gestor_db
    
    def crear(self, cliente_id):
        """Crea un nuevo pedido"""
        sql = f"INSERT INTO {TABLA_PEDIDOS} (cliente_id) VALUES (?)"
        if self.db.ejecutar(sql, (cliente_id,)):
            print(f"✓ Pedido creado (ID: {self.db.obtener_ultimo_id()})")
            return self.db.obtener_ultimo_id()
        return None
    
    def agregar_item(self, pedido_id, producto_id, cantidad):
        """Agrega un producto al pedido"""
        # Obtener precio actual del producto
        producto = self.db.obtener_todos(
            f"SELECT precio FROM {TABLA_PRODUCTOS} WHERE id = ?",
            (producto_id,)
        )
        
        if not producto:
            print(f"✗ Producto no existe")
            return False
        
        precio_unitario = producto[0]['precio']
        subtotal = precio_unitario * cantidad
        
        sql = f"""
        INSERT INTO {TABLA_DETALLES_PEDIDO} 
        (pedido_id, producto_id, cantidad, precio_unitario, subtotal)
        VALUES (?, ?, ?, ?, ?)
        """
        
        return self.db.ejecutar(sql, (pedido_id, producto_id, cantidad, precio_unitario, subtotal))
    
    def obtener_detalles(self, pedido_id):
        """Obtiene detalles de un pedido"""
        sql = f"""
        SELECT dp.*, p.nombre as producto_nombre
        FROM {TABLA_DETALLES_PEDIDO} dp
        JOIN {TABLA_PRODUCTOS} p ON dp.producto_id = p.id
        WHERE dp.pedido_id = ?
        """
        return self.db.obtener_todos(sql, (pedido_id,))
    
    def calcular_total(self, pedido_id):
        """Calcula el total de un pedido"""
        sql = f"""
        SELECT SUM(subtotal) as total
        FROM {TABLA_DETALLES_PEDIDO}
        WHERE pedido_id = ?
        """
        resultado = self.db.obtener_uno(sql, (pedido_id,))
        return resultado['total'] if resultado and resultado['total'] else 0
    
    def actualizar_total(self, pedido_id):
        """Actualiza el total en la tabla pedidos"""
        total = self.calcular_total(pedido_id)
        sql = f"UPDATE {TABLA_PEDIDOS} SET total = ? WHERE id = ?"
        return self.db.ejecutar(sql, (total, pedido_id))
    
    def cambiar_estado(self, pedido_id, nuevo_estado):
        """Cambia el estado de un pedido"""
        estados_validos = ['Pendiente', 'Procesando', 'Enviado', 'Entregado', 'Cancelado']
        if nuevo_estado not in estados_validos:
            print(f"✗ Estado no válido. Válidos: {', '.join(estados_validos)}")
            return False
        
        sql = f"UPDATE {TABLA_PEDIDOS} SET estado = ? WHERE id = ?"
        return self.db.ejecutar(sql, (nuevo_estado, pedido_id))
    
    def obtener_pedidos_cliente(self, cliente_id):
        """Obtiene todos los pedidos de un cliente"""
        sql = f"""
        SELECT * FROM {TABLA_PEDIDOS}
        WHERE cliente_id = ?
        ORDER BY fecha_pedido DESC
        """
        return self.db.obtener_todos(sql, (cliente_id,))
    
    def obtener_todos(self):
        """Obtiene todos los pedidos"""
        sql = f"""
        SELECT p.*, c.nombre as cliente_nombre
        FROM {TABLA_PEDIDOS} p
        JOIN {TABLA_CLIENTES} c ON p.cliente_id = c.id
        ORDER BY p.fecha_pedido DESC
        """
        return self.db.obtener_todos(sql)
    
    def pedidos_por_estado(self, estado):
        """Obtiene pedidos por estado"""
        sql = f"""
        SELECT p.*, c.nombre as cliente_nombre
        FROM {TABLA_PEDIDOS} p
        JOIN {TABLA_CLIENTES} c ON p.cliente_id = c.id
        WHERE p.estado = ?
        ORDER BY p.fecha_pedido DESC
        """
        return self.db.obtener_todos(sql, (estado,))
    
    def ingresos_totales(self):
        """Calcula ingresos totales de pedidos entregados"""
        sql = f"""
        SELECT SUM(total) as ingresos
        FROM {TABLA_PEDIDOS}
        WHERE estado = 'Entregado'
        """
        resultado = self.db.obtener_uno(sql)
        return resultado['ingresos'] if resultado and resultado['ingresos'] else 0

# ===== CONSULTAS AVANZADAS =====

def consultas_avanzadas(db):
    """
    Ejemplos de consultas SQL avanzadas
    """
    print("\n=== CONSULTAS AVANZADAS ===\n")
    
    # 1. Productos más vendidos
    print("1. Productos más vendidos:")
    sql = f"""
    SELECT p.nombre, SUM(dp.cantidad) as cantidad_vendida, SUM(dp.subtotal) as ingresos
    FROM {TABLA_PRODUCTOS} p
    LEFT JOIN {TABLA_DETALLES_PEDIDO} dp ON p.id = dp.producto_id
    GROUP BY p.id
    ORDER BY cantidad_vendida DESC
    LIMIT 5
    """
    resultados = db.obtener_todos(sql)
    for fila in resultados:
        if fila['cantidad_vendida']:
            print(f"   {fila['nombre']}: {fila['cantidad_vendida']} unidades - ${fila['ingresos']:.2f}")
    
    # 2. Clientes con más compras
    print("\n2. Clientes con más compras:")
    sql = f"""
    SELECT c.nombre, COUNT(p.id) as pedidos, SUM(p.total) as gasto_total
    FROM {TABLA_CLIENTES} c
    LEFT JOIN {TABLA_PEDIDOS} p ON c.id = p.cliente_id
    GROUP BY c.id
    ORDER BY gasto_total DESC
    LIMIT 5
    """
    resultados = db.obtener_todos(sql)
    for fila in resultados:
        if fila['pedidos']:
            print(f"   {fila['nombre']}: {fila['pedidos']} pedidos - ${fila['gasto_total']:.2f}")
    
    # 3. Promedio de pedidos por cliente
    print("\n3. Estadísticas de pedidos:")
    sql = f"""
    SELECT 
        COUNT(DISTINCT cliente_id) as total_clientes,
        COUNT(*) as total_pedidos,
        AVG(total) as promedio_pedido,
        MAX(total) as pedido_maximo
    FROM {TABLA_PEDIDOS}
    """
    resultado = db.obtener_uno(sql)
    if resultado:
        print(f"   Total clientes: {resultado['total_clientes']}")
        print(f"   Total pedidos: {resultado['total_pedidos']}")
        print(f"   Promedio por pedido: ${resultado['promedio_pedido']:.2f}")
        print(f"   Pedido máximo: ${resultado['pedido_maximo']:.2f}")

# ===== FUNCIÓN PARA MOSTRAR INFORMACIÓN DE TABLA =====

def mostrar_estructura_tabla(db, nombre_tabla):
    """
    Muestra la estructura de una tabla
    """
    sql = f"PRAGMA table_info({nombre_tabla})"
    columnas = db.obtener_todos(sql)
    
    print(f"\nEstructura de tabla '{nombre_tabla}':")
    for col in columnas:
        print(f"  {col['name']:20} {col['type']:10} (nullable: {bool(col['notnull'])})")

# ===== FUNCIONES DE DEMOSTRACIÓN =====

def cargar_datos_ejemplo(db, gestor_clientes, gestor_productos, gestor_pedidos):
    """
    Carga datos de ejemplo en la base de datos
    """
    print("\n=== CARGANDO DATOS DE EJEMPLO ===\n")
    
    # Clientes
    print("Creando clientes...")
    cliente_ids = []
    clientes = [
        ("Juan García", "juan@email.com", "555-0001", "Calle Principal 123"),
        ("María López", "maria@email.com", "555-0002", "Avenida Central 456"),
        ("Carlos Rodríguez", "carlos@email.com", "555-0003", "Plaza Mayor 789"),
    ]
    
    for nombre, email, telefono, direccion in clientes:
        cid = gestor_clientes.crear(nombre, email, telefono, direccion)
        if cid:
            cliente_ids.append(cid)
    
    # Productos
    print("\nCreando productos...")
    producto_ids = []
    productos = [
        ("Laptop Dell", 899.99, 5, "Laptop high performance", "Electrónica"),
        ("Mouse Logitech", 29.99, 50, "Mouse inalámbrico", "Accesorios"),
        ("Teclado Mecánico", 99.99, 20, "Teclado RGB", "Accesorios"),
        ("Monitor LG", 299.99, 10, "Monitor 4K 27 pulgadas", "Electrónica"),
        ("Auriculares Sony", 149.99, 15, "Auriculares con cancelación de ruido", "Audio"),
    ]
    
    for nombre, precio, stock, desc, cat in productos:
        pid = gestor_productos.crear(nombre, precio, stock, desc, cat)
        if pid:
            producto_ids.append(pid)
    
    # Pedidos
    print("\nCreando pedidos...")
    if cliente_ids and producto_ids:
        # Pedido 1
        pedido1 = gestor_pedidos.crear(cliente_ids[0])
        if pedido1:
            gestor_pedidos.agregar_item(pedido1, producto_ids[0], 1)
            gestor_pedidos.agregar_item(pedido1, producto_ids[1], 2)
            gestor_pedidos.actualizar_total(pedido1)
            gestor_pedidos.cambiar_estado(pedido1, 'Entregado')
        
        # Pedido 2
        pedido2 = gestor_pedidos.crear(cliente_ids[1])
        if pedido2:
            gestor_pedidos.agregar_item(pedido2, producto_ids[2], 1)
            gestor_pedidos.agregar_item(pedido2, producto_ids[4], 1)
            gestor_pedidos.actualizar_total(pedido2)
            gestor_pedidos.cambiar_estado(pedido2, 'Enviado')
        
        # Pedido 3
        pedido3 = gestor_pedidos.crear(cliente_ids[2])
        if pedido3:
            gestor_pedidos.agregar_item(pedido3, producto_ids[3], 1)
            gestor_pedidos.actualizar_total(pedido3)

def menu_interactivo(db, gestor_clientes, gestor_productos, gestor_pedidos):
    """
    Menú interactivo para gestionar la tienda
    """
    
    while True:
        print("\n" + "="*60)
        print("=== SISTEMA DE GESTIÓN TIENDA ONLINE ===")
        print("="*60)
        print("\n--- CLIENTES ---")
        print("1. Crear cliente")
        print("2. Ver todos los clientes")
        print("3. Buscar cliente por email")
        print("\n--- PRODUCTOS ---")
        print("4. Crear producto")
        print("5. Ver todos los productos")
        print("6. Ver productos bajo stock")
        print("7. Estadísticas de productos")
        print("\n--- PEDIDOS ---")
        print("8. Crear pedido")
        print("9. Ver todos los pedidos")
        print("10. Ver pedidos de un cliente")
        print("11. Ver detalle de pedido")
        print("12. Cambiar estado de pedido")
        print("\n--- REPORTES ---")
        print("13. Consultas avanzadas")
        print("14. Mostrar estructura de tablas")
        print("15. Ver información de base de datos")
        print("\n16. Salir")
        print("="*60)
        
        opcion = input("\nElige una opción (1-16): ").strip()
        
        try:
            if opcion == "1":
                print("\n--- CREAR CLIENTE ---")
                nombre = input("Nombre: ")
                email = input("Email: ")
                telefono = input("Teléfono (o Enter para omitir): ") or None
                direccion = input("Dirección (o Enter para omitir): ") or None
                
                if gestor_clientes.crear(nombre, email, telefono, direccion):
                    print(f"✓ Cliente creado exitosamente")
            
            elif opcion == "2":
                print("\n--- TODOS LOS CLIENTES ---")
                clientes = gestor_clientes.obtener_todos()
                if clientes:
                    print(f"\nTotal: {len(clientes)} clientes\n")
                    for cliente in clientes:
                        print(f"ID: {cliente['id']}")
                        print(f"  Nombre: {cliente['nombre']}")
                        print(f"  Email: {cliente['email']}")
                        print(f"  Teléfono: {cliente['telefono']}")
                        print(f"  Dirección: {cliente['direccion']}")
                        print(f"  Registro: {cliente['fecha_registro']}\n")
                else:
                    print("No hay clientes registrados")
            
            elif opcion == "3":
                print("\n--- BUSCAR CLIENTE ---")
                email = input("Email a buscar: ")
                cliente = gestor_clientes.buscar_por_email(email)
                if cliente:
                    print(f"\n✓ Cliente encontrado:")
                    print(f"  ID: {cliente['id']}")
                    print(f"  Nombre: {cliente['nombre']}")
                    print(f"  Email: {cliente['email']}")
                else:
                    print("✗ Cliente no encontrado")
            
            elif opcion == "4":
                print("\n--- CREAR PRODUCTO ---")
                nombre = input("Nombre: ")
                precio = float(input("Precio: $"))
                stock = int(input("Stock: "))
                descripcion = input("Descripción (o Enter para omitir): ") or None
                categoria = input("Categoría (o Enter para omitir): ") or None
                
                if gestor_productos.crear(nombre, precio, stock, descripcion, categoria):
                    print(f"✓ Producto creado")
            
            elif opcion == "5":
                print("\n--- TODOS LOS PRODUCTOS ---")
                productos = gestor_productos.obtener_todos()
                if productos:
                    print(f"\nTotal: {len(productos)} productos\n")
                    for prod in productos:
                        print(f"ID: {prod['id']} | {prod['nombre']}")
                        print(f"  Precio: ${prod['precio']:.2f}")
                        print(f"  Stock: {prod['stock']} unidades")
                        if prod['descripcion']:
                            print(f"  Descripción: {prod['descripcion']}")
                        if prod['categoria']:
                            print(f"  Categoría: {prod['categoria']}\n")
                else:
                    print("No hay productos")
            
            elif opcion == "6":
                print("\n--- PRODUCTOS BAJO STOCK ---")
                limite = int(input("Límite de stock (default 10): ") or "10")
                productos = gestor_productos.productos_bajo_stock(limite)
                if productos:
                    for prod in productos:
                        print(f"  {prod['nombre']}: {prod['stock']} unidades (${prod['precio']:.2f})")
                else:
                    print("Todos los productos tienen stock adecuado")
            
            elif opcion == "7":
                print("\n--- ESTADÍSTICAS DE PRODUCTOS ---")
                stats = gestor_productos.estadisticas()
                if stats:
                    print(f"  Total de productos: {stats['total']}")
                    print(f"  Precio promedio: ${stats['precio_promedio']:.2f}" if stats['precio_promedio'] else "  Precio promedio: N/A")
                    print(f"  Precio mínimo: ${stats['precio_minimo']:.2f}" if stats['precio_minimo'] else "  Precio mínimo: N/A")
                    print(f"  Precio máximo: ${stats['precio_maximo']:.2f}" if stats['precio_maximo'] else "  Precio máximo: N/A")
                    print(f"  Stock total: {stats['stock_total']}" if stats['stock_total'] else "  Stock total: 0")
            
            elif opcion == "8":
                print("\n--- CREAR PEDIDO ---")
                cliente_id = int(input("ID del cliente: "))
                if gestor_clientes.obtener(cliente_id):
                    pedido_id = gestor_pedidos.crear(cliente_id)
                    if pedido_id:
                        while True:
                            agregar = input("¿Agregar producto al pedido? (s/n): ").lower()
                            if agregar != 's':
                                break
                            producto_id = int(input("ID del producto: "))
                            cantidad = int(input("Cantidad: "))
                            if gestor_pedidos.agregar_item(pedido_id, producto_id, cantidad):
                                print("✓ Producto agregado")
                        
                        if gestor_pedidos.actualizar_total(pedido_id):
                            total = gestor_pedidos.calcular_total(pedido_id)
                            print(f"✓ Pedido creado con total: ${total:.2f}")
                else:
                    print("✗ Cliente no existe")
            
            elif opcion == "9":
                print("\n--- TODOS LOS PEDIDOS ---")
                pedidos = gestor_pedidos.obtener_todos()
                if pedidos:
                    for pedido in pedidos:
                        print(f"Pedido #{pedido['id']} - {pedido['cliente_nombre']}")
                        print(f"  Fecha: {pedido['fecha_pedido']}")
                        print(f"  Estado: {pedido['estado']}")
                        print(f"  Total: ${pedido['total']:.2f}\n")
                else:
                    print("No hay pedidos")
            
            elif opcion == "10":
                print("\n--- PEDIDOS DE UN CLIENTE ---")
                cliente_id = int(input("ID del cliente: "))
                pedidos = gestor_pedidos.obtener_pedidos_cliente(cliente_id)
                if pedidos:
                    for pedido in pedidos:
                        print(f"Pedido #{pedido['id']}")
                        print(f"  Fecha: {pedido['fecha_pedido']}")
                        print(f"  Estado: {pedido['estado']}")
                        print(f"  Total: ${pedido['total']:.2f}\n")
                else:
                    print("No hay pedidos para este cliente")
            
            elif opcion == "11":
                print("\n--- DETALLE DE PEDIDO ---")
                pedido_id = int(input("ID del pedido: "))
                detalles = gestor_pedidos.obtener_detalles(pedido_id)
                if detalles:
                    total = 0
                    for detalle in detalles:
                        print(f"  {detalle['producto_nombre']}")
                        print(f"    Cantidad: {detalle['cantidad']}")
                        print(f"    Precio unit.: ${detalle['precio_unitario']:.2f}")
                        print(f"    Subtotal: ${detalle['subtotal']:.2f}\n")
                        total += detalle['subtotal']
                    print(f"TOTAL: ${total:.2f}")
                else:
                    print("No hay detalles para este pedido")
            
            elif opcion == "12":
                print("\n--- CAMBIAR ESTADO DE PEDIDO ---")
                pedido_id = int(input("ID del pedido: "))
                print("Estados disponibles: Pendiente, Procesando, Enviado, Entregado, Cancelado")
                nuevo_estado = input("Nuevo estado: ")
                if gestor_pedidos.cambiar_estado(pedido_id, nuevo_estado):
                    print("✓ Estado actualizado")
            
            elif opcion == "13":
                consultas_avanzadas(db)
            
            elif opcion == "14":
                print("\n--- ESTRUCTURAS DE TABLAS ---")
                tablas = [TABLA_CLIENTES, TABLA_PRODUCTOS, TABLA_PEDIDOS, TABLA_DETALLES_PEDIDO]
                for tabla in tablas:
                    mostrar_estructura_tabla(db, tabla)
            
            elif opcion == "15":
                print("\n--- INFORMACIÓN DE BASE DE DATOS ---")
                print(f"Archivo: {DB_PATH}")
                print(f"Ruta: {Path(DB_PATH).absolute()}")
                if Path(DB_PATH).exists():
                    tamaño = Path(DB_PATH).stat().st_size
                    print(f"Tamaño: {tamaño / 1024:.2f} KB")
                
                # Contar registros en cada tabla
                print("\nRegistros por tabla:")
                for tabla in [TABLA_CLIENTES, TABLA_PRODUCTOS, TABLA_PEDIDOS]:
                    sql = f"SELECT COUNT(*) as total FROM {tabla}"
                    resultado = db.obtener_uno(sql)
                    print(f"  {tabla}: {resultado['total']}")
            
            elif opcion == "16":
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
    print("SISTEMA DE GESTIÓN TIENDA ONLINE CON SQLITE")
    print("="*60)
    
    # Inicializar gestor de base de datos
    gestor_db = GestorBaseDatos(DB_PATH)
    
    if gestor_db.conectar():
        # Crear tablas
        gestor_db.crear_tablas()
        
        # Inicializar gestores específicos
        gestor_clientes = GestorClientes(gestor_db)
        gestor_productos = GestorProductos(gestor_db)
        gestor_pedidos = GestorPedidos(gestor_db)
        
        # Cargar datos de ejemplo si es la primera ejecución
        if gestor_clientes.contar() == 0:
            cargar_datos_ejemplo(gestor_db, gestor_clientes, gestor_productos, gestor_pedidos)
        
        # Ejecutar menú interactivo
        menu_interactivo(gestor_db, gestor_clientes, gestor_productos, gestor_pedidos)
        
        # Cerrar conexión
        gestor_db.desconectar()
    else:
        print("No se pudo conectar a la base de datos")

# === DESAFÍOS ADICIONALES ===
# 1. Implementar búsquedas por rango de fechas
# 2. Agregar descuentos a los pedidos
# 3. Implementar carrito de compras temporal
# 4. Crear sistema de valoraciones de productos
# 5. Implementar respaldo y restauración de base de datos
