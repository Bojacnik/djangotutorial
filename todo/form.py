from django.db import models
from django import forms
from .models import User, Task


class UserCreateForm(forms.ModelForm):
    is_active = forms.BooleanField(label='Is active: ', required=False)
    email = forms.CharField(label='E-mail: ', max_length=100)
    password = forms.CharField(label='Password: ', widget=forms.PasswordInput)

    class Meta(object):
        model = User
        exclude = [
            'created_at'
            'updated_at'
        ]


class UserUpdateForm(forms.ModelForm):
    email = forms.CharField(label='E-mail: ', max_length=100)
    password = forms.CharField(label='Password: ', widget=forms.PasswordInput)

    class Meta(object):
        model = User
        exclude = [
            'created_at',
            'updated_at'
        ]


class TaskCreateForm(forms.ModelForm):
    is_completed = forms.BooleanField(label='Is completed: ', required=False)
    title = forms.CharField(label='Title: ', max_length=100)

    class Meta(object):
        model = Task
        exclude = [
            'created_at'
            'updated_at'
        ]


class TaskUpdateForm(forms.ModelForm):
    is_completed = forms.BooleanField(label='Is completed', required=False)
    owner = forms.ModelChoiceField(User.objects.filter())
    title = forms.CharField(label="Title", max_length=100)

    class Meta(object):
        model = Task
        exclude = [
            'created_at',
            'updated_at'
        ]



