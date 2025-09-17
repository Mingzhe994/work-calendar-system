from flask import Blueprint, render_template
from models import Task, Workflow

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """主页路由"""
    tasks = Task.query.order_by(Task.due_date).limit(5).all()
    workflows = Workflow.query.all()
    return render_template('index.html', tasks=tasks, workflows=workflows)