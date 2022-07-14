"""djangotutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from todo.views import UserCreateView, UserCreateView, UserListView, UserUpdateView, UserDeleteView, UserDetailView
from todo.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/', UserListView.as_view(), name="users-list"),
    path('users/create', UserCreateView.as_view(), name="user-create"),
    path('users/<int:pk>', UserDetailView.as_view(), name="user-detail"),  # should not end with detail, cuz standards or something
    path('users/<int:pk>/update', UserUpdateView.as_view(), name="user-update"),
    path('users/<int:pk>/delete', UserDeleteView.as_view(), name="user-delete"),

    path('tasks/', TaskListView.as_view(), name="tasks-list"),
    path('tasks/create', TaskCreateView.as_view()),
    path('tasks/<int:pk>', TaskDetailView.as_view()),
    path('tasks/<int:pk>/update', TaskUpdateView.as_view()),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view())
]
