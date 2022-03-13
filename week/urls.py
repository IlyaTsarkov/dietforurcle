from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.days_of_week, name='days_of_week'),
]

