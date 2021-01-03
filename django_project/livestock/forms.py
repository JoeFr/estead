from django import forms
from .models import Animal, AnimalLog, AnimalHarvest


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = "__all__"


class AnimalLogForm(forms.ModelForm):
    class Meta:
        model = AnimalLog
        fields = "__all__"


class AnimalHarvestForm(forms.ModelForm):
    class Meta:
        model = AnimalHarvest
        fields = "__all__"
