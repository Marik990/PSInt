from rest_framework import serializers
from Lombard.models import Klienci, Przedmioty, Zamowienia


class KlienciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klienci
        fields = '__all__'

class PrzedmiotySerializer(serializers.ModelSerializer):
    class Meta:
        model = Przedmioty
        fields = '__all__'


class ZamowieniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zamowienia
        fields = '__all__'
