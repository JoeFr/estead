from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from django.views.generic import ListView, DetailView
from django.contrib import messages
from finances.models import Expense


class ProjectList(ListView):
    template_name = 'projects/projects.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        return Project.objects.all()


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter()
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] = Expense.objects.filter()
        return context

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['expenses_sum'] = Expense.objects.all().aggregate(sum_all=Sum('total')).get('sum_all')
        return context


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Project has been created')
            return redirect('projects:projects')
    else:
        form = ProjectForm()

    return render(request, 'projects/project-create.html', {'form': form})


def edit_project(request, pk, template_name='projects/project-edit.html'):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        messages.success(request, f'Project has been saved')
        return redirect('projects:projects')
    else:
        messages.error(request, f'Something went wrong')
    return render(request, template_name, {'form': form})


def delete_project(request, pk, template_name='projects/project-delete.html'):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, f'Project has been deleted')
        return redirect('projects:projects')
    return render(request, template_name, {'object': project})


# Task stuff


class TaskList(ListView):
    template_name = 'projects/tasks.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        return Task.objects.all()


class TaskDetailView(DetailView):
    model = Task
    template_name = 'projects/task.html'


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Task has been created')
            return redirect('projects:tasks')
    else:
        form = TaskForm()

    return render(request, 'projects/task-create.html', {'form': form})


def edit_task(request, pk, template_name='projects/task-edit.html'):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        messages.success(request, f'Task has been saved')
        return redirect('projects:tasks')
    return render(request, template_name, {'form': form})


def delete_task(request, pk, template_name='projects/task-delete.html'):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, f'Task has been deleted')
        return redirect('tasks')
    return render(request, template_name, {'object': task})
