# Ejercicio 23 - Interfaces Gráficas con Tkinter

## ¿Qué es Tkinter?
Tkinter es la biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI). Viene incluida con Python, no requiere instalación externa y permite desarrollar aplicaciones de escritorio con ventanas, botones, menús y controles interactivos.

## Objetivos del ejercicio
- Dominar widgets principales (Label, Button, Entry, Text, Canvas, etc.)
- Aprender gestores de diseño (pack, grid, place)
- Manejo de eventos (clics, teclas, ventanas emergentes)
- Crear múltiples ventanas independientes
- Implementar menús y diálogos

## Estructura de la aplicación
`ejercicio23.py` contiene 5 aplicaciones integradas:

### 1. **Calculadora**
- Widgets: Button, Entry, StringVar
- Funcionalidad: Operaciones aritméticas (+, -, *, /), sqrt, pow
- Validación: Captura de errores en expresiones inválidas
- Layout: Grid de botones con pack()

```python
button = tk.Button(root, text="7", command=lambda: agregar("7"))
button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
```

### 2. **Editor de Texto**
- Widgets: Text, Menu, Menubutton
- Funcionalidad: Nuevo, Abrir, Guardar, Guardar como, Deshacer/Rehacer
- Diálogos: filedialog.askopenfilename(), filedialog.asksaveasfilename()
- Manejo de archivos: Lectura/escritura UTF-8

```python
menubar = tk.Menu(root)
root.config(menu=menubar)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Guardar", command=guardar)
```

### 3. **Gestor de Formularios**
- Widgets: Entry, Spinbox, Combobox, Radiobutton, Checkbutton, Text
- Funcionalidad: Validación de datos, procesamiento y visualización
- Validación: Email con "@", campos obligatorios
- Widgets avanzados: ttk.Spinbox (0-120), ttk.Combobox (países)

```python
self.edad = ttk.Spinbox(frame, from_=0, to=120, width=10)
self.pais = ttk.Combobox(frame, values=["México", "España", ...])
```

### 4. **Dibujador con Canvas**
- Widget: Canvas
- Funcionalidad: Dibujo libre con ratón, selección de color, guardar imagen
- Eventos: Button-1 (inicio), B1-Motion (movimiento)
- Diálogos: colorchooser.askcolor()

```python
self.canvas.bind("<Button-1>", self.iniciar_dibujo)
self.canvas.bind("<B1-Motion>", self.dibujar)
```

### 5. **Aplicación Principal**
- Menú central que abre cada aplicación en ventana independiente (Toplevel)
- Navegación entre módulos sin cerrar la ventana principal

## Widgets principales explicados

| Widget | Uso | Ejemplo |
|--------|-----|---------|
| **Label** | Texto estático | `tk.Label(root, text="Hola")` |
| **Button** | Botón clickeable | `tk.Button(root, text="OK", command=funcion)` |
| **Entry** | Campo de texto | `entrada = tk.Entry(root)` |
| **Text** | Área multilínea | `texto = tk.Text(root, height=10, width=50)` |
| **Frame** | Contenedor | `marco = tk.Frame(root)` |
| **Canvas** | Área de dibujo | `lienzo = tk.Canvas(root, bg="white")` |
| **Listbox** | Lista seleccionable | `lista = tk.Listbox(root)` |
| **Checkbutton** | Casilla | `ttk.Checkbutton(root, text="Opción")` |
| **Radiobutton** | Opción exclusiva | `ttk.Radiobutton(root, text="Sí")` |
| **Combobox** | Desplegable | `ttk.Combobox(root, values=["A", "B"])` |
| **Spinbox** | Selector numérico | `ttk.Spinbox(root, from_=0, to=100)` |
| **Scale** | Deslizador | `tk.Scale(root, from_=0, to=100)` |

## Gestores de layout

### **pack()**: Organización en bloques
```python
button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5)
```

### **grid()**: Filas y columnas
```python
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
button.grid(row=0, column=1)
```

### **place()**: Posicionamiento absoluto
```python
button.place(x=50, y=100, width=200, height=30)
```

## Variables especiales de Tkinter

```python
# StringVar para Entry/Label vinculados
nombre = tk.StringVar()
entrada = tk.Entry(root, textvariable=nombre)
valor = nombre.get()  # obtener
nombre.set("nuevo valor")  # establecer

# IntVar para Spinbox
edad = tk.IntVar()
spinner = tk.Spinbox(root, textvariable=edad)

# BooleanVar para Checkbutton
opcion = tk.BooleanVar()
check = tk.Checkbutton(root, variable=opcion)
if opcion.get():  # True o False
    print("Seleccionado")
```

## Eventos comunes

| Evento | Descripción |
|--------|-------------|
| `<Button-1>` | Clic izquierdo del ratón |
| `<Button-3>` | Clic derecho |
| `<Double-1>` | Doble clic |
| `<Key>` | Cualquier tecla |
| `<Return>` | Tecla Enter |
| `<Escape>` | Tecla Escape |
| `<FocusIn>` | Widget recibe foco |
| `<FocusOut>` | Widget pierde foco |
| `<Configure>` | Ventana cambia tamaño |

Ejemplo de binding:
```python
widget.bind('<Button-1>', lambda e: accion(e.x, e.y))
widget.bind('<Key>', lambda e: tecla_presionada(e.char))
```

## Diálogos y ventanas emergentes

```python
# Información
messagebox.showinfo("Título", "Mensaje informativo")

# Advertencia
messagebox.showwarning("Advertencia", "Cuidado")

# Error
messagebox.showerror("Error", "Algo salió mal")

# Pregunta (True/False)
if messagebox.askyesno("Confirmar", "¿Continuar?"):
    print("Sí")

# Abrir archivo
archivo = filedialog.askopenfilename(filetypes=[("Texto", "*.txt")])

# Guardar archivo
archivo = filedialog.asksaveasfilename(defaultextension=".txt")

# Seleccionar color
color = colorchooser.askcolor(title="Color")
```

## Ejecución

### Instalación (no requiere dependencias externas)
Tkinter viene incluido con Python. Si no lo tienes, instala:

**Windows:**
```powershell
# Ya incluido en instalador estándar de Python
python -m tkinter  # Prueba rápida
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-tk
```

**macOS:**
```bash
# Ya incluido en instalador oficial de Python
```

### Ejecutar aplicación
```powershell
cd c:\Users\SENA\Desktop\phyton\ 2\ 18
python ejercicio23.py
```

La ventana principal mostrará 4 botones para acceder a cada aplicación.

## Mejores prácticas

1. **Organiza widgets en clases**: Facilita mantenimiento
2. **Usa Frames para agrupar**: Mejor estructura visual
3. **Valida entrada de usuario**: Previene errores
4. **Captura excepciones**: Manejo de errores robusto
5. **Documenta eventos**: Indica qué acciones disparan qué funciones
6. **Usa ttk para mejor apariencia**: ttk.Button, ttk.Entry se ven más modernos

## Ejemplos adicionales

### Crear ventana secundaria
```python
ventana_nueva = tk.Toplevel(root)
ventana_nueva.title("Nueva ventana")
tk.Label(ventana_nueva, text="Contenido").pack()
```

### Ejecutar función después de tiempo
```python
root.after(2000, lambda: print("2 segundos después"))
```

### Manejar cierre de ventana
```python
def al_cerrar():
    if messagebox.askyesno("Salir", "¿Cerrar aplicación?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", al_cerrar)
```

### Frame con barra de desplazamiento
```python
frame_principal = ttk.Frame(root)
canvas = tk.Canvas(frame_principal)
scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
canvas.config(yscrollcommand=scrollbar.set)

frame_interior = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame_interior, anchor="nw")

frame_principal.pack(fill=tk.BOTH, expand=True)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
```

---

**Extensiones sugeridas:**
- Añadir persistencia (guardar datos en JSON o BD)
- Integrar con librerías como `Pillow` para procesamiento de imágenes
- Crear temas personalizados con `ttkbootstrap`
- Implementar drag-and-drop
