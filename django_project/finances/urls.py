from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "finances"

urlpatterns = [
    path('expenses/', login_required(views.ExpenseList.as_view(), login_url='/accounts/login/'), name='expenses'),
    path('expenses/<int:pk>/', login_required(views.ExpenseDetailView.as_view(), login_url='/accounts/login/'), name='expense'),
    path('expenses/edit/<int:pk>/', login_required(views.edit_expense, login_url='/accounts/login/'), name='edit_expense'),
    path('expenses/create/', login_required(views.create_expense, login_url='/accounts/login/'), name='create_expense'),
    path('expenses/delete/<int:pk>/', login_required(views.delete_expense, login_url='/accounts/login/'), name='delete_expense'),
]
