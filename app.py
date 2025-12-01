from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Configuración
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Cambia esta clave por una más segura en producción
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev_secret_key_123')

db = SQLAlchemy(app)

# Modelo
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done,
            'created_at': self.created_at.isoformat()
        }


# Rutas web
@app.route('/')
def index():
    username = session.get('username')
    return render_template('index.html', username=username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        if username:
            session['username'] = username
            flash(f'Bienvenido, {username}!', 'success')
            return redirect(url_for('index'))
        flash('Por favor ingresa un nombre.', 'warning')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Sesión cerrada.', 'info')
    return redirect(url_for('index'))


@app.route('/tasks')
def list_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('tasks.html', tasks=tasks)


@app.route('/tasks/new', methods=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        if not title:
            flash('El título es obligatorio.', 'danger')
            return redirect(url_for('new_task'))
        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        flash('Tarea creada correctamente.', 'success')
        return redirect(url_for('list_tasks'))
    return render_template('task_form.html', action='Crear', task=None)


@app.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.title = request.form.get('title', task.title).strip()
        task.description = request.form.get('description', task.description).strip()
        task.done = True if request.form.get('done') == 'on' else False
        db.session.commit()
        flash('Tarea actualizada.', 'success')
        return redirect(url_for('list_tasks'))
    return render_template('task_form.html', action='Editar', task=task)


@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Tarea eliminada.', 'info')
    return redirect(url_for('list_tasks'))


# API REST (JSON)
@app.route('/api/tasks', methods=['GET'])
def api_get_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return jsonify([t.to_dict() for t in tasks])


@app.route('/api/tasks', methods=['POST'])
def api_create_task():
    if not request.json or 'title' not in request.json:
        abort(400, description='JSON inválido o falta campo "title"')
    title = request.json.get('title')
    description = request.json.get('description', '')
    task = Task(title=title, description=description)
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def api_get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task.to_dict())


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def api_update_task(task_id):
    task = Task.query.get_or_404(task_id)
    if not request.json:
        abort(400, description='JSON inválido')
    task.title = request.json.get('title', task.title)
    task.description = request.json.get('description', task.description)
    task.done = request.json.get('done', task.done)
    db.session.commit()
    return jsonify(task.to_dict())


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def api_delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'result': True})


# Inicialización de la base de datos al ejecutar directamente
if __name__ == '__main__':
    # Crear base de datos si no existe
    with app.app_context():
        db.create_all()
    app.run(debug=True)
