# Generated by Django 4.2.2 on 2023-06-09 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoGym', '0004_usuarios_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='activo',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='contraseña',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='correo',
        ),
    ]
