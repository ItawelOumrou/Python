# Generated by Django 4.0.3 on 2022-03-18 00:08

import Reconnaissande_de_visage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reconnaissande_de_visage', '0005_alter_etudiants_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiants',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=Reconnaissande_de_visage.models.filepath),
        ),
    ]