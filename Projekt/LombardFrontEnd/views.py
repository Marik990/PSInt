from django.shortcuts import render


# Create your views here.

def przedmiotyList(request):
    return render(request, 'frontend/przedmioty-list.html')
