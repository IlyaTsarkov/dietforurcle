from django.shortcuts import render
from .models import Week
from menu.models import Menu

# Create your views here.
def days_of_week(request):
    week = Week.objects.all()
    menu = Menu.objects.all()
    return render(request, 'week/index.html', {'week': week, 'menu': menu})

