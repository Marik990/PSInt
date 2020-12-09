from datetime import date

from django.db import models


# Create your models here.

class Klienci(models.Model):
    idKlienta = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    numerTelefonu = models.IntegerField()
    email = models.EmailField()
    adres = models.CharField(max_length=255)
    login = models.CharField(max_length=45, null=False)
    haslo = models.CharField(max_length=45, null=False)

    class Meta:
        db_table = "klienci"


class Przedmioty(models.Model):
    idPrzedmiotu = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=255, null=False)
    cena = models.DecimalField(max_digits=11, decimal_places=2, null=False)
    opis = models.TextField()
    widoczny = models.BooleanField(default=True)

    class Meta:
        db_table = "przedmioty"


class Zamowienia(models.Model):
    idZamowienia = models.AutoField(primary_key=True)
    idKlienta = models.ForeignKey(Klienci, on_delete=models.CASCADE, db_column="idKlienta")
    idPrzedmiotu = models.ForeignKey(Przedmioty, on_delete=models.CASCADE, db_column="idPrzedmiotu")
    dataZamowienia = models.DateTimeField(default=date.today)
    status = models.CharField(max_length=255)

    class Meta:
        db_table = "zamowienia"
