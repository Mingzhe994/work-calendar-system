from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Task, Workflow, Comment
from datetime import datetime

# 创建蓝图
main_bp = Blueprint('main', __name__)
task_bp = Blueprint('task', __name__, url_prefix='/tasks')
workflow_bp = Blueprint('workflow', __name__, url_prefix='/workflows')
issue_bp = Blueprint('issue', __name__, url_prefix='/issues')
analytics_bp = Blueprint('analytics', __name__, url_prefix='/analytics')

# 主页路由
@main_bp.route('/')
def index():
    tasks = Task.query.order_by(Task.due_date).limit(5).all()
    workflows = Workflow.query.all()
    return render_template('index.html', tasks=tasks, workflows=workflows)

# 任务相关路由
@task_bp.route('/')
def list_tasks():
    tasks = Task.query.all()
    return render_template('tasks/list.html', tasks=tasks)

@task_bp.route('/<int:task_id>')
def view_task(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template('tasks/view.html', task=task)

@task_bp.route('/create', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        status = request.form.get('status', 'pending')
        priority = request.form.get('priority', 'medium')
        due_date_str = request.form.get('due_date')
        workflow_id = request.form.get('workflow_id')
        
        due_date = None
        if due_date_str:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
        
        task = Task(
            title=title,
            description=description,
            status=status,
            priority=priority,
            due_date=due_date,
            workflow_id=workflow_id
        )
        
        db.session.add(task)
        db.session.commit()
        
        flash('任务创建成功！', 'success')
        return redirect(url_for('task.list_tasks'))
    
    workflows = Workflow.query.all()
    return render_template('tasks/create.html', workflows=workflows)

# 工作流相关路由
@workflow_bp.route('/')
def list_workflows():
    workflows = Workflow.query.all()
    return render_template('workflows/list.html', workflows=workflows)

@workflow_bp.route('/<int:workflow_id>')
def view_workflow(workflow_id):
    workflow = Workflow.query.get_or_404(workflow_id)
    return render_template('workflows/view.html', workflow=workflow)

# 分析相关路由
@analytics_bp.route('/')
def dashboard():
    # 任务统计
    total_tasks = Task.query.count()
    completed_tasks = Task.query.filter_by(status='completed').count()
    pending_tasks = Task.query.filter_by(status='pending').count()
    in_progress_tasks = Task.query.filter_by(status='in_progress').count()
    
    # 工作流统计
    workflows = Workflow.query.all()
    workflow_stats = []
    for workflow in workflows:
        workflow_stats.append({
            'name': workflow.name,
            'task_count': workflow.tasks.count()
        })
    
    return render_template(
        'analytics/dashboard.html',
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks,
        in_progress_tasks=in_progress_tasks,
        workflow_stats=workflow_stats
    )