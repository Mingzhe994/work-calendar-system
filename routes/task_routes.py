from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from models import db, Task, Workflow, Comment
from datetime import datetime

task_bp = Blueprint('task', __name__, url_prefix='/tasks')

@task_bp.route('/')
def list_tasks():
    """任务列表"""
    tasks = Task.query.all()
    return render_template('tasks/list.html', tasks=tasks)

@task_bp.route('/<int:task_id>')
def view_task(task_id):
    """查看任务详情"""
    task = Task.query.get_or_404(task_id)
    return render_template('tasks/view.html', task=task)

@task_bp.route('/create', methods=['GET', 'POST'])
def create_task():
    """创建任务"""
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

@task_bp.route('/<int:task_id>/update', methods=['GET', 'POST'])
def update_task(task_id):
    """更新任务"""
    task = Task.query.get_or_404(task_id)
    
    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        task.status = request.form.get('status')
        task.priority = request.form.get('priority')
        due_date_str = request.form.get('due_date')
        task.workflow_id = request.form.get('workflow_id')
        
        if due_date_str:
            task.due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
        
        db.session.commit()
        flash('任务更新成功！', 'success')
        return redirect(url_for('task.view_task', task_id=task.id))
    
    workflows = Workflow.query.all()
    return render_template('tasks/update.html', task=task, workflows=workflows)

@task_bp.route('/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    """删除任务"""
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('任务已删除！', 'success')
    return redirect(url_for('task.list_tasks'))