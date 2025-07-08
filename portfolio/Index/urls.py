from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
     path('upload/', views.upload_project, name='upload_project'),
     path('project/<int:pk>/', views.project_detail, name='project_detail'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('register/', views.register, name='register'),

]