from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobardOverview, name="lombard-overview"),
    path('przedmioty-list/', views.przedmiotyList, name="przedmioty-list"),
    path('przedmioty-detail/<str:pk>/', views.przedmiotyDetail, name="przedmioty-detail"),
    path('przedmioty-create/', views.przedmiotyCreate, name="przedmioty-create"),
    path('przedmioty-update/<str:pk>/', views.przedmiotyUpdate, name="przedmioty-update"),
    path('przedmioty-delete/<str:pk>/', views.przedmiotyDelete, name="przedmioty-delete"),
]