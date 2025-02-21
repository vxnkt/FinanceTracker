from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.shortcuts import render
from .models import Expense



def expense_list(request):
    expenses = Expense.objects.order_by('-date')
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    if expense:
        expense.delete()
    return redirect('expense_list')

def expense_list(request):
    category_filter = request.GET.get('category', '')  # Get selected category from URL
    expenses = Expense.objects.all()
    
    if category_filter:
        expenses = expenses.filter(category=category_filter)  # Filter expenses by category

    categories = Expense.objects.values_list('category', flat=True).distinct()  # Get unique categories

    return render(request, 'expenses/expense_list.html', {
        'expenses': expenses,
        'categories': categories,
    })

