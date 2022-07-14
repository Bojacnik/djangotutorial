from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from django.urls import reverse_lazy

from todo.models import User, Task
from todo.form import UserCreateForm, UserUpdateForm
from todo.form import TaskCreateForm, TaskUpdateForm


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class UserCreateView(CreateView):
    model = User
    template_name = 'user_create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('users-list')


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'


class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_update.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('users-list')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('users-list')


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_create.html'
    form_class = TaskCreateForm
    success_url = reverse_lazy('tasks-list')


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_update.html'
    form_class = TaskUpdateForm
    success_url = reverse_lazy('tasks-list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('tasks-list')
