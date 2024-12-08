from flask import Flask
from app.database import init_db
from app.routes import task_routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos
    init_db(app)

    # Registrar el blueprint de rutas
    app.register_blueprint(task_routes)

    # Ruta raíz adicional para verificar que el servidor funciona
    @app.route("/")
    def home():
        return {
            "message": "Welcome to the ToDoList API!",
            "endpoints": {
                "create_task": {"method": "POST", "path": "/tasks"},
                "list_tasks": {"method": "GET", "path": "/tasks"},
                "update_task": {"method": "PATCH", "path": "/tasks/<int:id>"},
                "delete_task": {"method": "DELETE", "path": "/tasks/<int:id>"}
            }
        }

    return app
