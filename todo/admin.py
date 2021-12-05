from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title']
    readonly_fields = ['created']


admin.site.register(Todo, TodoAdmin)
