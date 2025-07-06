from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('upload/', views.upload_project, name='upload_project'),
     path('project/<int:pk>/', views.project_detail, name='project_detail'),
]