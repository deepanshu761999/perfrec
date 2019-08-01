"""pfmansys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.Create_New, name='create'),
    path('login/', views.User_Login, name='login'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/create', views.create_course, name='create_course'),
    path('<int:id>', views.course_board, name='course_board'),
    path('delete_test/<int:course_id>/<int:test_id>', views.delete_test, name='delete_test'),
]
