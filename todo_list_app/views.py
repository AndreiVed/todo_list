from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo_list_app.forms import TaskForm
from todo_list_app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list_app/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list_app:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list_app:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list_app:index")


class TaskToggleView(generic.View):
    @staticmethod
    def post(request, pk):
        task = Task.objects.get(pk=pk)
        task.is_completed = not task.is_completed
        task.save()
        return redirect("todo_list_app:index")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list_app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list_app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list_app:tag-list")

