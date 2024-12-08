from flask import Blueprint, request, jsonify
from app.models import Task
from app.database import db

task_routes = Blueprint('tasks', __name__)

@task_routes.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = Task(title=data['title'], description=data['description'])
    db.session.add(task)
    db.session.commit()
    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status
    }), 201

@task_routes.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([
        {"id": t.id, "title": t.title, "description": t.description, "status": t.status}
        for t in tasks
    ])

@task_routes.route('/tasks/<int:id>', methods=['PATCH'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.json

    if "title" in data:
        task.title = data["title"]
    if "description" in data:
        task.description = data["description"]
    if "status" in data:
        task.status = data["status"]
    db.session.commit()
    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status
    })


@task_routes.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"}), 200
