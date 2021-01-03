from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
from django.views.generic import ListView, DetailView
from django.contrib import messages


class ExpenseList(ListView):
    template_name = 'finances/expenses.html'
    context_object_name = 'expense_list'

    def get_context_data(self, **kwargs):
        context = super(ExpenseList, self).get_context_data(**kwargs)
        context['expenses_sum'] = Expense.objects.all().aggregate(sum_all=Sum('total')).get('sum_all')
        return context

    def get_queryset(self):
        return Expense.objects.all()


class ExpenseDetailView(DetailView):
    model = Expense
    template_name = 'finances/expense.html'


def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Expense has been created')
            return redirect('finances:expenses')
    else:
        form = ExpenseForm()

    return render(request, 'finances/expense-create.html', {'form': form})


def edit_expense(request, pk, template_name='finances/expense-edit.html'):
    expense = get_object_or_404(Expense, pk=pk)
    form = ExpenseForm(request.POST or None, instance=expense)
    if form.is_valid():
        form.save()
        messages.success(request, f'Expense has been saved')
        return redirect('finances:expenses')
    return render(request, template_name, {'form': form})


def delete_expense(request, pk, template_name='finances/expense-delete.html'):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, f'Expense has been deleted')
        return redirect('expenses')
    return render(request, template_name, {'object': expense})
