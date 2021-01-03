import uuid

from django.db import models
from django.conf import settings


class ProjectTags(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Status(models.Model):
    title = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(default='default-project.jpg', upload_to='projects')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    start_date = models.DateField(null=True, blank=True)
    deadline_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(ProjectTags, blank=True)
    completed = models.BooleanField(default=False)
    budget = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    actual_cost = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    order = models.IntegerField(blank=False, default=100_000)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default='default-task.jpg', upload_to='tasks')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default='Not Planned')
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, related_name='task_project', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
