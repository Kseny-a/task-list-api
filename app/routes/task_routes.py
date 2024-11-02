from flask import Blueprint, abort, make_response
from app.models.task import Task

tasks_bp = Blueprint("tasks_bp", __name__, url_prefix="/tasks")

# @tasks_bp.get("")
# def get_all_tasks():
#     tasks_response = []
#     for task in tasks:
#         tasks_response.append(
#             {
#                 "id": task.id,
#                 "title": task.title,
#                 "description": task.description,
#                 "completed_at": task.completed_at 
#             }
#         )
#     return tasks_response

# @tasks_bp.get("/<task_id>")
# def get_one_task(task_id):
#     task = validate_task_id(task_id)

#     return {
#                 "id": task.id,
#                 "title": task.title,
#                 "description": task.description,
#                 "completed_at": task.completed_at 
#             }

# def validate_task_id()
#     try:
#         task_id = int(task_id)
#     except:
#         response =  {"message": "Task {task_id} invalid."}
#         abort(make_response(response, 400))  

#     for task in tasks:
#         if task.id == task_id:
#             return task
        
#     response =  {"message": "Task {task_id} not found."}
#     abort(make_response(response, 404))      




