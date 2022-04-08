from django.db import models
import datetime
import os

def filepath(request,filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s", (timeNow , old_filename)
    return os.path.join('images/',filename)

class niveau(models.Model):
    nom = models.CharField(max_length=20)

    class Meta:
        db_table ="reconnaissande_de_visage_niveau"

class filiere(models.Model):
    nom = models.CharField(max_length=20)
    niveau = models.ForeignKey(niveau, on_delete=models.CASCADE)

    class Meta:
        db_table ="reconnaissande_de_visage_filiere"

class etudiants(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_Naissance = models.DateField()
    nni= models.IntegerField()
    email = models.EmailField(unique=True)
    telephone = models.IntegerField(unique=True)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    """niveau = models.ForeignKey(niveau, on_delete=models.CASCADE)
    filiere = models.ForeignKey(filiere, on_delete=models.CASCADE)"""


