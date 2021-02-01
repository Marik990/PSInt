from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Przedmioty
from .serializers import PrzedmiotySerializer


# Create your views here.

@api_view(['GET'])
def lobardOverview(request):
    api_urls = {
        'List': '/przedmioty-list/',
        'Detail View': '/przedmioty-detail/<str:pk>/',
        'Create': '/przedmioty-create/',
        'Update': '/przedmioty-update/<str:pk>/',
        'Delete': '/przedmioty-delete/<str:ph>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def przedmiotyList(request):
    przedmioty = Przedmioty.objects.all().order_by('-idPrzedmiotu')
    serializer = PrzedmiotySerializer(przedmioty, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def przedmiotyDetail(request, pk):
    przedmioty = Przedmioty.objects.get(idPrzedmiotu=pk)
    serializer = PrzedmiotySerializer(przedmioty, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def przedmiotyCreate(request):
    serializer = PrzedmiotySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def przedmiotyUpdate(request, pk):
    przedmiot = Przedmioty.objects.get(idPrzedmiotu=pk)
    serializer = PrzedmiotySerializer(instance=przedmiot, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def przedmiotyDelete(request, pk):
    przedmiot = Przedmioty.objects.get(idPrzedmiotu=pk)
    przedmiot.delete()

    return Response('Przedmiot został usunięty!')
