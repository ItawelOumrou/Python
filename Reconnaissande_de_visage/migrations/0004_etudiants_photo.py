# Generated by Django 4.0.3 on 2022-03-17 17:24

import Reconnaissande_de_visage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reconnaissande_de_visage', '0003_remove_etudiants_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiants',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=Reconnaissande_de_visage.models.filepath),
        ),
    ]
