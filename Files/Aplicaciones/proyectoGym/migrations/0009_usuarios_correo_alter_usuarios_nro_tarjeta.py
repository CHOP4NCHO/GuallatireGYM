# Generated by Django 4.2.1 on 2023-06-13 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoGym', '0008_usuarios_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='correo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nro_tarjeta',
            field=models.CharField(default='0000000000000000', max_length=16, verbose_name='Número de tarjeta'),
        ),
    ]
