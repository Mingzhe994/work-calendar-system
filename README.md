# 工作日历系统

一个用于管理工作流和任务的日历系统。

## 功能特点

- 工作流管理：创建和管理不同类型的工作流
- 任务管理：创建、分配和跟踪任务
- 日历视图：以日历形式查看任务和截止日期
- 数据分析：分析任务完成情况和工作效率

## 技术栈

- 后端：Flask, SQLAlchemy
- 前端：HTML, CSS, JavaScript, Bootstrap
- 数据库：SQLite

## 安装和运行

1. 克隆仓库
```
git clone https://github.com/Mingzhe994/work-calendar-system.git
cd work-calendar-system
```

2. 安装依赖
```
pip install -r requirements.txt
```

3. 运行应用
```
python app.py
```

4. 访问应用
```
http://localhost:5005
```

## 项目结构

- `/models`: 数据模型
- `/routes`: 路由和视图函数
- `/services`: 业务逻辑服务
- `/static`: 静态文件（CSS, JavaScript）
- `/templates`: HTML模板
- `/tests`: 测试文件

## 许可证

MIT