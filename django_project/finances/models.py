from django.db import models
from django.conf import settings
from datetime import date


class ExpenseTags(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class ExpenseStatus(models.Model):
    title = models.CharField(max_length=30)
    style = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Expense(models.Model):
    title = models.CharField(max_length=200)
    supplier = models.CharField(max_length=100, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    date = models.DateField(default=date.today)
    total = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    receipt = models.ImageField(default='default-task.jpg', upload_to='tasks')
    status = models.ForeignKey(ExpenseStatus, on_delete=models.CASCADE, default='Not Planned')
    purchaser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey('projects.Project', related_name='project_expense', on_delete=models.CASCADE, null=True, blank=True)
    task = models.ForeignKey('projects.Task', related_name='task_expense', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
