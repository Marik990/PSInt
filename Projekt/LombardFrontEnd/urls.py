from django.urls import path
from . import views

urlpatterns = [
    path('przedmioty/', views.przedmiotyList, name="przedmioty-list"),
]