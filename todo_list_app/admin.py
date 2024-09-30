from django.contrib import admin

from todo_list_app.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "content",
        "deadline",
        "is_completed",]
    search_fields = ["content", ]


@admin.register(Tag)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]
