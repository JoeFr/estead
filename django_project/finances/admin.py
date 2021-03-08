from django.contrib import admin
from .models import Expense, ExpenseTags, ExpenseStatus

admin.site.register(Expense)
admin.site.register(ExpenseTags)
admin.site.register(ExpenseStatus)
