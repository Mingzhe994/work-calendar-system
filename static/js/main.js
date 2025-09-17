// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    // 初始化Bootstrap提示工具
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // 任务状态切换
    const statusButtons = document.querySelectorAll('.status-toggle');
    if (statusButtons) {
        statusButtons.forEach(button => {
            button.addEventListener('click', function() {
                const taskId = this.getAttribute('data-task-id');
                const newStatus = this.getAttribute('data-status');
                updateTaskStatus(taskId, newStatus);
            });
        });
    }

    // 日期选择器初始化
    const datePickers = document.querySelectorAll('.datepicker');
    if (datePickers) {
        datePickers.forEach(picker => {
            picker.flatpickr({
                dateFormat: "Y-m-d",
                allowInput: true
            });
        });
    }
});

// 更新任务状态
function updateTaskStatus(taskId, status) {
    fetch(`/tasks/${taskId}/status`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify({ status: status })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // 更新UI
            const statusBadge = document.querySelector(`#task-${taskId}-status`);
            if (statusBadge) {
                // 移除所有状态相关的类
                statusBadge.classList.remove('bg-secondary', 'bg-warning', 'bg-success');
                
                // 添加新状态对应的类
                if (status === 'pending') {
                    statusBadge.classList.add('bg-secondary');
                    statusBadge.textContent = '待处理';
                } else if (status === 'in_progress') {
                    statusBadge.classList.add('bg-warning');
                    statusBadge.textContent = '进行中';
                } else if (status === 'completed') {
                    statusBadge.classList.add('bg-success');
                    statusBadge.textContent = '已完成';
                }
            }
            
            // 显示成功消息
            showAlert('任务状态已更新', 'success');
        } else {
            // 显示错误消息
            showAlert('更新任务状态失败: ' + data.message, 'danger');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showAlert('更新任务状态时发生错误', 'danger');
    });
}

// 显示提示消息
function showAlert(message, type) {
    const alertContainer = document.getElementById('alert-container');
    if (!alertContainer) {
        // 如果容器不存在，创建一个
        const container = document.createElement('div');
        container.id = 'alert-container';
        container.style.position = 'fixed';
        container.style.top = '20px';
        container.style.right = '20px';
        container.style.zIndex = '9999';
        document.body.appendChild(container);
    }
    
    const alert = document.createElement('div');
    alert.className = `alert alert-${type} alert-dismissible fade show`;
    alert.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    document.getElementById('alert-container').appendChild(alert);
    
    // 5秒后自动关闭
    setTimeout(() => {
        alert.classList.remove('show');
        setTimeout(() => {
            alert.remove();
        }, 150);
    }, 5000);
}