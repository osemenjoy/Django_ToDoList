from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', TaskList.as_view(), name = 'tasks' ),
    path('create/', TaskCreate.as_view(), name= 'task-create'),
    path('edit/<int:pk>', TaskUpdate.as_view(), name = 'task-update'),
    path('delete/<int:pk>', TaskDelete.as_view(), name= 'task-delete')
]