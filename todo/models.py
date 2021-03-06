from django.db import models
from django.core.validators import validate_email


class User(models.Model):
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    updated_at = models.DateTimeField(blank=False, null=False, auto_now=True)  # FIX ME: some wierd shit
    is_active = models.BooleanField(default=False, null=False)
    email = models.EmailField(blank=False, null=True, validators=[validate_email])
    password = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.email


class Task(models.Model):
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    update_at = models.DateTimeField(blank=False, null=False, auto_now=True)
    is_completed = models.BooleanField(default=False, null=False)
    owner = models.ForeignKey("User", on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=70, blank=False, null=False)

    def __str__(self) -> str:
        return self.title

