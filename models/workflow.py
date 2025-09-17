from datetime import datetime
from models import db

class Workflow(db.Model):
    """工作流模型"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)
    
    # 关联关系
    tasks = db.relationship('Task', backref='workflow', lazy='dynamic')
    
    def __repr__(self):
        return f'<Workflow {self.name}>'
    
    def to_dict(self):
        """转换为字典"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'task_count': self.tasks.count()
        }