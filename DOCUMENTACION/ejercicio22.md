# Ejercicio 22 - Desarrollo Web con Flask

## ¿Qué es Flask?
Flask es un microframework en Python para crear aplicaciones web ligeras y extensibles. Permite definir rutas, manejar peticiones HTTP, renderizar plantillas y conectarse a bases de datos.

## Objetivos del ejercicio
- Construir una aplicación de gestión de tareas (CRUD)
- Exponer una API REST para las mismas tareas
- Usar sesiones y mensajes `flash`
- Persistir datos en SQLite con `Flask_SQLAlchemy`

## Estructura del proyecto
```
mi_app/
  app.py
  requirements.txt
  templates/
    base.html
    index.html
    login.html
    tasks.html
    task_form.html
  static/
    css/style.css
  DOCUMENTACION/ejercicio22.md
```

## Dependencias
Instala las dependencias en tu entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecutar la aplicación
```powershell
python app.py
# Abrir http://localhost:5000
```

## Rutas principales
- `GET /` - Página principal
- `GET, POST /login` - Iniciar sesión (guarda `session['username']`)
- `GET /logout` - Cerrar sesión
- `GET /tasks` - Lista de tareas
- `GET, POST /tasks/new` - Crear nueva tarea
- `GET, POST /tasks/<id>/edit` - Editar tarea
- `POST /tasks/<id>/delete` - Eliminar tarea

## API REST
- `GET /api/tasks` - Lista JSON
- `POST /api/tasks` - Crear (JSON: `{ "title": "...", "description": "..." }`)
- `GET /api/tasks/<id>` - Obtener tarea
- `PUT /api/tasks/<id>` - Actualizar tarea (JSON)
- `DELETE /api/tasks/<id>` - Eliminar tarea

Ejemplo con `curl` (crear tarea):
```powershell
curl -X POST http://localhost:5000/api/tasks -H "Content-Type: application/json" -d '{"title":"Comprar leche","description":"Ir al supermercado"}'
```

## Notas
- La app usa `sqlite:///tasks.db` y crea la BD automáticamente la primera vez.
- En producción, cambia `app.secret_key` por una clave segura y configura despliegue con WSGI (gunicorn, waitress) y variable de entorno `FLASK_SECRET_KEY`.

---
Si quieres, puedo:
- Añadir autenticación simple (usuario/contraseña) con `Flask-Login`.
- Crear tests para la API.
- Preparar un `Dockerfile` para desplegar la app.
