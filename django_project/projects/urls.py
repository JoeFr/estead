from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    path('projects/', login_required(views.ProjectList.as_view(), login_url='/accounts/login/'), name="projects"),
    path('projects/<int:pk>/', login_required(views.ProjectDetailView.as_view(), login_url='/accounts/login/'), name="project"),
    path('projects/edit/<int:pk>/', login_required(views.edit_project, login_url='/accounts/login/'), name='edit_project'),
    path('projects/create/', login_required(views.create_project, login_url='/accounts/login/'), name='create_project'),
    path('projects/delete/<int:pk>/', login_required(views.delete_project, login_url='/accounts/login/'), name='delete_project'),
    path('tasks/', login_required(views.TaskList.as_view(), login_url='/accounts/login/'), name='tasks'),
    path('tasks/<int:pk>/', login_required(views.TaskDetailView.as_view(), login_url='/accounts/login/'), name='task'),
    path('tasks/edit/<int:pk>/', login_required(views.edit_task, login_url='/accounts/login/'), name='edit_task'),
    path('tasks/create/', login_required(views.create_task, login_url='/accounts/login/'), name='create_task'),
    path('tasks/delete/<int:pk>/', login_required(views.delete_task, login_url='/accounts/login/'), name='delete_task'),
]
