# Generated by Django 4.2.2 on 2023-06-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGYM', '0003_remove_usuarios_fecha_exp_alter_usuarios_nro_tarjeta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='activo',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='hora',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
