# Generated by Django 4.2.5 on 2023-11-26 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas_medicas', '0006_alter_citamedica_hora_alter_citamedica_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='citamedica',
            name='estado',
            field=models.CharField(choices=[('PROGRAMADA', 'Programada'), ('ATENDIDA', 'Atendida')], default='PROGRAMADA', max_length=20),
        ),
    ]