"""
URL configuration for todo_list_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from todo_list_app.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView, TaskToggleView,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "task/<int:pk>/create/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),

    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list",
        ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name = "tag-create",
    ), path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ), path(
        "tags/<int:pk>/create/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
    path(
        "tasks/<int:pk>/toggle/",
        TaskToggleView.as_view(),
        name="task-toggle"
    ),
]

app_name = "todo_list_app"
