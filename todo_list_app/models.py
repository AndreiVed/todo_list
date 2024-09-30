from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=68, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)
    deadline = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tags")

    class Meta:
        ordering = ["-created_date"]
