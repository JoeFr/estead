from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "livestock"

urlpatterns = [
    path('animals/', login_required(views.AnimalList.as_view(), login_url='/accounts/login/'), name='animals'),
    path('animals/<int:pk>/', login_required(views.AnimalDetailView.as_view(), login_url='/accounts/login/'), name='animal'),
    path('animals/edit/<int:pk>/', login_required(views.edit_animal, login_url='/accounts/login/'), name='edit_animal'),
    path('animals/create/', login_required(views.create_animal, login_url='/accounts/login/'), name='create_animal'),
    path('animals/delete/<int:pk>/', login_required(views.delete_animal, login_url='/accounts/login/'), name='delete_animal'),
    path('animal-harvests/', login_required(views.AnimalHarvestList.as_view(), login_url='/accounts/login/'), name='animal_harvests'),
    path('animal-harvests/<int:pk>/', login_required(views.AnimalHarvestDetailView.as_view(), login_url='/accounts/login/'), name='animal_harvest'),
    path('animal-harvests/edit/<int:pk>/', login_required(views.edit_animal_harvest, login_url='/accounts/login/'), name='edit_animal_harvest'),
    path('animal-harvests/create/', login_required(views.create_animal_harvest, login_url='/accounts/login/'), name='create_animal_harvest'),
    path('animal-harvests/delete/<int:pk>/', login_required(views.delete_animal_harvest, login_url='/accounts/login/'), name='delete_animal_harvest'),
]
