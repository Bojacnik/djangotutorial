from django.contrib import admin

from todo import models


class UserAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Task, TaskAdmin)
