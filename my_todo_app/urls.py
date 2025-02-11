from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create_task/', views.create_task, name='create_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
]