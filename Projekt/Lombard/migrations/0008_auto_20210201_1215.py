# Generated by Django 3.1.4 on 2021-02-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lombard', '0007_przedmioty_opis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='przedmioty',
            name='opis',
            field=models.TextField(default=''),
        ),
    ]
