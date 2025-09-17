import os
from datetime import timedelta

class Config:
    """基础配置类"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 数据库配置
    @staticmethod
    def get_database_uri():
        """获取数据库URI"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return 'sqlite:///' + os.path.join(base_dir, 'instance', 'work_calendar.db')
    
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    
    # 应用配置
    DEBUG = True
    PORT = 5005

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True

class TestingConfig(Config):
    """测试环境配置"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False
    
# 配置映射
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}