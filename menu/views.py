from django.shortcuts import render
from .models import Menu


# Create your views here.
def home(request):
    menu = Menu.objects.all()
    return render(request, 'menu/index.html', {'menu': menu})

