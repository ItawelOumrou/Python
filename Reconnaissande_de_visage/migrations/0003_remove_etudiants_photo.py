# Generated by Django 4.0.3 on 2022-03-17 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reconnaissande_de_visage', '0002_alter_etudiants_moyenne_bac'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiants',
            name='photo',
        ),
    ]
