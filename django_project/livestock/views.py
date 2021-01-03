from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal, AnimalType, AnimalStatus, AnimalHealth, AnimalLog, AnimalHarvest, MeatType
from .forms import AnimalForm, AnimalLogForm, AnimalHarvestForm
from django.db.models import Sum
from django.views.generic import ListView, DetailView
from django.contrib import messages


class AnimalList(ListView):
    template_name = 'livestock/animals.html'
    context_object_name = 'animal_list'

    def get_queryset(self):
        return Animal.objects.all()


class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'livestock/animal.html'


def create_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Animal has been created')
            return redirect('livestock:animals')
    else:
        form = AnimalForm()

    return render(request, 'livestock/animal-create.html', {'form': form})


def edit_animal(request, pk, template_name='livestock/animal-edit.html'):
    animal = get_object_or_404(Animal, pk=pk)
    form = AnimalForm(request.POST or None, instance=animal)
    if form.is_valid():
        form.save()
        messages.success(request, f'Animal has been saved')
        return redirect('livestock:animals')
    return render(request, template_name, {'form': form})


def delete_animal(request, pk, template_name='livestock/animal-delete.html'):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        animal.delete()
        messages.success(request, f'Animal has been deleted')
        return redirect('animals')
    return render(request, template_name, {'object': animal})


class AnimalLogList(ListView):
    template_name = 'livestock/animal-logs.html'
    context_object_name = 'animal_log_list'

    def get_queryset(self):
        return AnimalLog.objects.all()


class AnimalLogDetailView(DetailView):
    model = AnimalLog
    template_name = 'livestock/animal-log.html'


def create_animal_log(request):
    if request.method == 'POST':
        form = AnimalLogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Animal log has been created')
            return redirect('livestock:animal_logs')
    else:
        form = AnimalLogForm()

    return render(request, 'livestock/animal-log-create.html', {'form': form})


def edit_animal_log(request, pk, template_name='livestock/animal-log-edit.html'):
    animallog = get_object_or_404(AnimalLog, pk=pk)
    form = AnimalLogForm(request.POST or None, instance=animallog)
    if form.is_valid():
        form.save()
        messages.success(request, f'Animal log has been saved')
        return redirect('livestock:animal-logs')
    return render(request, template_name, {'form': form})


def delete_animal_log(request, pk, template_name='livestock/animal-log-delete.html'):
    animallog = get_object_or_404(AnimalLog, pk=pk)
    if request.method == 'POST':
        animallog.delete()
        messages.success(request, f'AnimalLog has been deleted')
        return redirect('animal_logs')
    return render(request, template_name, {'object': animallog})


class AnimalHarvestList(ListView):
    template_name = 'livestock/animal-harvests.html'
    context_object_name = 'animal_harvest_list'

    def get_context_data(self, **kwargs):
        context = super(AnimalHarvestList, self).get_context_data(**kwargs)
        context['harvests_weight_sum'] = AnimalHarvest.objects.all().aggregate(sum_all=Sum('weight')).get('sum_all')
        return context

    def get_queryset(self):
        return AnimalHarvest.objects.all()


class AnimalHarvestDetailView(DetailView):
    model = AnimalHarvest
    template_name = 'livestock/animal-harvest.html'


def create_animal_harvest(request):
    if request.method == 'POST':
        form = AnimalHarvestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Animal harvest has been created')
            return redirect('livestock:animal_harvests')
    else:
        form = AnimalHarvestForm()

    return render(request, 'livestock/animal-harvest-create.html', {'form': form})


def edit_animal_harvest(request, pk, template_name='livestock/animal-harvest-edit.html'):
    animalharvest = get_object_or_404(AnimalHarvest, pk=pk)
    form = AnimalHarvestForm(request.POST or None, instance=animalharvest)
    if form.is_valid():
        form.save()
        messages.success(request, f'Animal harvest has been saved')
        return redirect('livestock:animal_harvests')
    return render(request, template_name, {'form': form})


def delete_animal_harvest(request, pk, template_name='livestock/animal-harvest-delete.html'):
    animalharvest = get_object_or_404(AnimalHarvest, pk=pk)
    if request.method == 'POST':
        animalharvest.delete()
        messages.success(request, f'Animal harvest has been deleted')
        return redirect('animal_harvests')
    return render(request, template_name, {'object': animalharvest})
