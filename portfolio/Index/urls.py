from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('upload/', views.upload_project, name='upload_project'),
]