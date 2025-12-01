import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser
import math

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora - Ejercicio 23")
        self.root.geometry("400x500")
        self.expresion = tk.StringVar()
        self.resultado = tk.StringVar()
        self.setup_ui()

    def setup_ui(self):
        # Pantalla de resultado
        display_frame = tk.Frame(self.root, bg="lightgray", height=60)
        display_frame.pack(fill=tk.X, padx=5, pady=5)

        tk.Label(display_frame, text="Expresión:", bg="lightgray").pack(anchor="w", padx=5)
        tk.Entry(display_frame, textvariable=self.expresion, font=("Arial", 14)).pack(fill=tk.X, padx=5, pady=2)

        tk.Label(display_frame, text="Resultado:", bg="lightgray").pack(anchor="w", padx=5)
        tk.Entry(display_frame, textvariable=self.resultado, font=("Arial", 14), state="readonly").pack(fill=tk.X, padx=5, pady=2)

        # Grid de botones
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        botones = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', 'sqrt', 'pow', 'DEL']
        ]

        for fila in botones:
            frame_fila = tk.Frame(btn_frame)
            frame_fila.pack(fill=tk.X, pady=2)
            for btn_txt in fila:
                if btn_txt == '=':
                    btn = tk.Button(frame_fila, text=btn_txt, font=("Arial", 12), bg="green", fg="white",
                                    command=self.calcular)
                elif btn_txt == 'C':
                    btn = tk.Button(frame_fila, text=btn_txt, font=("Arial", 12), bg="red", fg="white",
                                    command=self.limpiar)
                elif btn_txt == 'DEL':
                    btn = tk.Button(frame_fila, text=btn_txt, font=("Arial", 12), bg="orange", fg="white",
                                    command=self.borrar_ultimo)
                else:
                    btn = tk.Button(frame_fila, text=btn_txt, font=("Arial", 12),
                                    command=lambda x=btn_txt: self.agregar(x))
                btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2)

    def agregar(self, caracter):
        self.expresion.set(self.expresion.get() + caracter)

    def calcular(self):
        try:
            expr = self.expresion.get()
            expr = expr.replace("sqrt", "math.sqrt").replace("pow", "pow")
            resultado = eval(expr)
            self.resultado.set(resultado)
        except Exception as e:
            messagebox.showerror("Error", f"Expresión inválida: {e}")

    def limpiar(self):
        self.expresion.set("")
        self.resultado.set("")

    def borrar_ultimo(self):
        self.expresion.set(self.expresion.get()[:-1])


class EditorTextoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto - Ejercicio 23")
        self.root.geometry("600x400")
        self.archivo_abierto = None
        self.setup_ui()

    def setup_ui(self):
        # Menú
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Nuevo", command=self.nuevo)
        file_menu.add_command(label="Abrir", command=self.abrir)
        file_menu.add_command(label="Guardar", command=self.guardar)
        file_menu.add_command(label="Guardar como...", command=self.guardar_como)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit)

        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Editar", menu=edit_menu)
        edit_menu.add_command(label="Deshacer", command=self.deshacer)
        edit_menu.add_command(label="Rehacer", command=self.rehacer)

        # Área de texto
        self.texto = tk.Text(self.root, font=("Courier New", 11), wrap=tk.WORD)
        self.texto.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Barra de estado
        self.status = tk.Label(self.root, text="Listo", bg="lightgray", anchor="w")
        self.status.pack(fill=tk.X, side=tk.BOTTOM)

    def nuevo(self):
        self.texto.delete("1.0", tk.END)
        self.archivo_abierto = None
        self.root.title("Editor de Texto - [Sin guardar]")
        self.status.config(text="Nuevo archivo")

    def abrir(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"), ("Todos", "*.*")])
        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                self.texto.delete("1.0", tk.END)
                self.texto.insert("1.0", contenido)
                self.archivo_abierto = archivo
                self.root.title(f"Editor de Texto - {archivo}")
                self.status.config(text=f"Abierto: {archivo}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir: {e}")

    def guardar(self):
        if self.archivo_abierto:
            self.guardar_en(self.archivo_abierto)
        else:
            self.guardar_como()

    def guardar_como(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos", "*.*")])
        if archivo:
            self.guardar_en(archivo)

    def guardar_en(self, archivo):
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write(self.texto.get("1.0", tk.END))
            self.archivo_abierto = archivo
            self.root.title(f"Editor de Texto - {archivo}")
            self.status.config(text=f"Guardado: {archivo}")
            messagebox.showinfo("Éxito", "Archivo guardado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {e}")

    def deshacer(self):
        try:
            self.texto.edit_undo()
        except:
            pass

    def rehacer(self):
        try:
            self.texto.edit_redo()
        except:
            pass


class GestorFormuarios:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Formularios - Ejercicio 23")
        self.root.geometry("500x600")
        self.setup_ui()

    def setup_ui(self):
        # Frame principal con scrollbar
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(main_frame, text="Formulario de Registro", font=("Arial", 14, "bold")).pack(anchor="w", pady=10)

        # Nombre
        ttk.Label(main_frame, text="Nombre completo:").pack(anchor="w")
        self.nombre = ttk.Entry(main_frame, width=40)
        self.nombre.pack(anchor="w", pady=5)

        # Email
        ttk.Label(main_frame, text="Correo electrónico:").pack(anchor="w")
        self.email = ttk.Entry(main_frame, width=40)
        self.email.pack(anchor="w", pady=5)

        # Edad
        ttk.Label(main_frame, text="Edad:").pack(anchor="w")
        self.edad = ttk.Spinbox(main_frame, from_=0, to=120, width=10)
        self.edad.pack(anchor="w", pady=5)

        # País
        ttk.Label(main_frame, text="País:").pack(anchor="w")
        self.pais = ttk.Combobox(main_frame, values=["México", "España", "Argentina", "Chile", "Colombia"], width=37)
        self.pais.pack(anchor="w", pady=5)

        # Género
        ttk.Label(main_frame, text="Género:").pack(anchor="w", pady=(10, 5))
        self.genero = tk.StringVar(value="otro")
        ttk.Radiobutton(main_frame, text="Masculino", variable=self.genero, value="masculino").pack(anchor="w")
        ttk.Radiobutton(main_frame, text="Femenino", variable=self.genero, value="femenino").pack(anchor="w")
        ttk.Radiobutton(main_frame, text="Otro", variable=self.genero, value="otro").pack(anchor="w")

        # Intereses
        ttk.Label(main_frame, text="Intereses:", pady=(10, 5)).pack(anchor="w")
        self.intereses = {}
        for interes in ["Programación", "Deportes", "Música", "Viajes"]:
            var = tk.BooleanVar()
            ttk.Checkbutton(main_frame, text=interes, variable=var).pack(anchor="w")
            self.intereses[interes] = var

        # Botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(anchor="w", pady=20)
        ttk.Button(btn_frame, text="Enviar", command=self.enviar).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Limpiar", command=self.limpiar).pack(side=tk.LEFT, padx=5)

        # Resultado
        ttk.Label(main_frame, text="Resultado:", font=("Arial", 10, "bold")).pack(anchor="w", pady=(20, 5))
        self.resultado = tk.Text(main_frame, height=8, width=50, state="disabled")
        self.resultado.pack(fill=tk.BOTH, expand=True)

    def enviar(self):
        nombre = self.nombre.get().strip()
        email = self.email.get().strip()
        edad = self.edad.get()

        if not nombre or not email:
            messagebox.showwarning("Validación", "Por favor completa nombre y email")
            return

        if not "@" in email:
            messagebox.showwarning("Validación", "Email inválido")
            return

        seleccionados = [k for k, v in self.intereses.items() if v.get()]

        resultado_txt = f"Nombre: {nombre}\nEmail: {email}\nEdad: {edad}\nPaís: {self.pais.get()}\n"
        resultado_txt += f"Género: {self.genero.get()}\nIntereses: {', '.join(seleccionados)}"

        self.resultado.config(state="normal")
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert("1.0", resultado_txt)
        self.resultado.config(state="disabled")
        messagebox.showinfo("Éxito", "Formulario procesado")

    def limpiar(self):
        self.nombre.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.edad.delete(0, tk.END)
        self.pais.set("")
        self.genero.set("otro")
        for var in self.intereses.values():
            var.set(False)
        self.resultado.config(state="normal")
        self.resultado.delete("1.0", tk.END)
        self.resultado.config(state="disabled")


class DibujadorCanvas:
    def __init__(self, root):
        self.root = root
        self.root.title("Dibujador con Canvas - Ejercicio 23")
        self.root.geometry("700x600")
        self.color_actual = "black"
        self.setup_ui()

    def setup_ui(self):
        # Barra de herramientas
        toolbar = ttk.Frame(self.root)
        toolbar.pack(fill=tk.X, padx=5, pady=5)

        ttk.Button(toolbar, text="Seleccionar color", command=self.seleccionar_color).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="Limpiar", command=self.limpiar).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="Salvar imagen", command=self.salvar_imagen).pack(side=tk.LEFT, padx=5)

        # Canvas
        self.canvas = tk.Canvas(self.root, bg="white", cursor="crosshair")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.canvas.bind("<Button-1>", self.iniciar_dibujo)
        self.canvas.bind("<B1-Motion>", self.dibujar)

        self.x_anterior = None
        self.y_anterior = None

    def iniciar_dibujo(self, event):
        self.x_anterior = event.x
        self.y_anterior = event.y

    def dibujar(self, event):
        if self.x_anterior and self.y_anterior:
            self.canvas.create_line(self.x_anterior, self.y_anterior, event.x, event.y, fill=self.color_actual, width=2)
            self.x_anterior = event.x
            self.y_anterior = event.y

    def seleccionar_color(self):
        color = colorchooser.askcolor(title="Selecciona color")
        if color[1]:
            self.color_actual = color[1]

    def limpiar(self):
        self.canvas.delete("all")

    def salvar_imagen(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".ps", filetypes=[("PostScript", "*.ps")])
        if archivo:
            self.canvas.postscript(file=archivo)
            messagebox.showinfo("Éxito", f"Imagen guardada en {archivo}")


class AplicacionPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 23 - Tkinter GUI Completo")
        self.root.geometry("600x400")
        self.setup_ui()

    def setup_ui(self):
        # Título
        titulo = tk.Label(self.root, text="Ejercicio 23: Interfaces Gráficas con Tkinter", 
                         font=("Arial", 16, "bold"), bg="lightblue", pady=20)
        titulo.pack(fill=tk.X)

        # Botones para cada aplicación
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Button(btn_frame, text="Calculadora", font=("Arial", 12), 
                 command=self.abrir_calculadora, height=2, bg="green", fg="white").pack(fill=tk.X, pady=10)

        tk.Button(btn_frame, text="Editor de Texto", font=("Arial", 12), 
                 command=self.abrir_editor, height=2, bg="blue", fg="white").pack(fill=tk.X, pady=10)

        tk.Button(btn_frame, text="Formulario", font=("Arial", 12), 
                 command=self.abrir_formulario, height=2, bg="purple", fg="white").pack(fill=tk.X, pady=10)

        tk.Button(btn_frame, text="Dibujador", font=("Arial", 12), 
                 command=self.abrir_dibujador, height=2, bg="orange", fg="white").pack(fill=tk.X, pady=10)

        # Pie de página
        footer = tk.Label(self.root, text="Haz clic en cualquier botón para abrir la aplicación", 
                         bg="lightgray", fg="gray", pady=10)
        footer.pack(fill=tk.X, side=tk.BOTTOM)

    def abrir_calculadora(self):
        ventana = tk.Toplevel(self.root)
        CalculadoraApp(ventana)

    def abrir_editor(self):
        ventana = tk.Toplevel(self.root)
        EditorTextoApp(ventana)

    def abrir_formulario(self):
        ventana = tk.Toplevel(self.root)
        GestorFormuarios(ventana)

    def abrir_dibujador(self):
        ventana = tk.Toplevel(self.root)
        DibujadorCanvas(ventana)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionPrincipal(root)
    root.mainloop()
