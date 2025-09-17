from datetime import datetime
from models import db

class Task(db.Model):
    """任务模型"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')  # pending, in_progress, completed
    priority = db.Column(db.String(20), default='medium')  # low, medium, high
    due_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    # 关联关系
    workflow_id = db.Column(db.Integer, db.ForeignKey('workflow.id'))
    comments = db.relationship('Comment', backref='task', lazy='dynamic', cascade='all, delete-orphan')
    progress_history = db.relationship('TaskProgressHistory', backref='task', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Task {self.title}>'
    
    def to_dict(self):
        """转换为字典"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'priority': self.priority,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'workflow_id': self.workflow_id
        }