from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.geos import Point
from django.utils import timezone
from django.db.models import Manager as GeoManager
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Imagepath = os.path.join(BASE_DIR, 'defaut.jpg')

# Create your models here.
class Borne(models.Model):
    name = models.CharField(max_length=250)
    east = models.FloatField()
    nord = models.FloatField()
    picture = models.ImageField(default=Imagepath)#on utilise défault pour l'image par défaut
    geom = models.PointField(srid=4326)
    objects = GeoManager()

    def __unicode__(self):
        return self.name
    @property
    def picture_url(self):
        return self.picture.url

    class meta:
        verbose_name_plural = 'Bornes'

    def __str__(self):
        return self.name

class Region(models.Model):
    sce_geo = models.CharField(max_length=50)
    sce_sem = models.CharField(max_length=50)
    date = models.DateField()
    origine = models.CharField(max_length=50)
    region = models.CharField(max_length=3)
    nom = models.CharField(max_length=50)
    superficie = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def _unicode_(self):
        return self.nom

    def __str__(self):
        return self.nom
