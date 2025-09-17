from models import db, Workflow

class WorkflowService:
    """工作流服务类"""
    
    @staticmethod
    def initialize_default_workflows():
        """初始化默认工作流"""
        # 检查是否已存在工作流
        if Workflow.query.count() > 0:
            return
        
        # 创建默认工作流
        default_workflows = [
            {
                'name': '标准工作流',
                'description': '标准任务处理流程，适用于大多数工作任务'
            },
            {
                'name': '紧急工作流',
                'description': '用于处理紧急任务的工作流程，优先级更高'
            },
            {
                'name': '项目工作流',
                'description': '适用于长期项目的工作流程，包含更多阶段和审核'
            }
        ]
        
        for workflow_data in default_workflows:
            workflow = Workflow(**workflow_data)
            db.session.add(workflow)
        
        db.session.commit()
    
    @staticmethod
    def get_all_workflows():
        """获取所有工作流"""
        return Workflow.query.all()
    
    @staticmethod
    def get_workflow_by_id(workflow_id):
        """根据ID获取工作流"""
        return Workflow.query.get(workflow_id)
    
    @staticmethod
    def create_workflow(name, description):
        """创建新工作流"""
        workflow = Workflow(name=name, description=description)
        db.session.add(workflow)
        db.session.commit()
        return workflow
    
    @staticmethod
    def update_workflow(workflow_id, name, description):
        """更新工作流"""
        workflow = Workflow.query.get(workflow_id)
        if workflow:
            workflow.name = name
            workflow.description = description
            db.session.commit()
        return workflow
    
    @staticmethod
    def delete_workflow(workflow_id):
        """删除工作流"""
        workflow = Workflow.query.get(workflow_id)
        if workflow:
            db.session.delete(workflow)
            db.session.commit()
            return True
        return False