# Generated by Django 4.2.1 on 2023-06-28 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGYM', '0006_usuarios_altura_usuarios_imc_usuarios_peso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='altura',
            field=models.FloatField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='imc',
            field=models.FloatField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='peso',
            field=models.FloatField(blank=True, max_length=64),
        ),
    ]