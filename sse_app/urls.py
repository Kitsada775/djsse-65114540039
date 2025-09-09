from django.urls import path
from . import views

app_name = 'sse_app'

urlpatterns = [
    # Main progress page
    path('', views.ProgressTaskView.as_view(), name='progress'),
    
    # SSE endpoint for real-time progress updates
    path('progress-stream/', views.TaskProgressStreamView.as_view(), name='progress_stream'),
    
    # API endpoints
    path('api/start-task/', views.StartTaskView.as_view(), name='start_task'),
    path('api/task-status/', views.TaskStatusView.as_view(), name='task_status'),
]
