from flask import Blueprint, abort, make_response, request, Response
from app.models.goal import Goal
from ..db import db

goals_bp = Blueprint("goals_bp", __name__, url_prefix="/goals")

@goals_bp.get("")
def get_all_goals():
    query = db.select(Goal)
    goals = db.session.scalars(query)
    goals_response = []
    for goal in goals:
        goals_response.append(
            {
                "id": goal.id,
                "title": goal.title
            }
        )
    return goals_response, 200

@goals_bp.get("/<goal_id>")
def get_one_goal(goal_id):
    goal = validate_goal_id(goal_id)

    return {"goal":{
                "id": goal.id,
                "title": goal.title}
            }

def validate_goal_id(goal_id):
    try:
        goal_id = int(goal_id)
    except:
        response =  {"message": f"Goal {goal_id} invalid."}
        abort(make_response(response, 400))

    query = db.select(Goal).where(Goal.id==goal_id)
    goal = db.session.scalar(query)
    if not goal:
        response =  {"message": f"Goal {goal_id} not found."}
        abort(make_response(response, 404))   

    return goal    