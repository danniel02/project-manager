from django.urls import path
from . import views


app_name = 'view'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.ProjectView.as_view(), name="project"),
    path('<int:pk>/<int:task_id>/', views.TaskView.as_view(), name="task")
]