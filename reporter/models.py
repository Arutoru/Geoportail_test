from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.geos import Point
from django.utils import timezone
from django.db.models import Manager as GeoManager
import os

class Aot(models.Model):
    id_aot = models.IntegerField()
    amodiatair = models.CharField(max_length=50)
    rccm = models.CharField(max_length=50)
    niu = models.CharField(max_length=50)
    bp = models.CharField(max_length=50)
    tel = models.BigIntegerField()
    duree_bail = models.IntegerField()
    taux_loyer = models.IntegerField()
    sup = models.FloatField()
    mont_cauti = models.BigIntegerField()
    date_caut = models.DateField()
    geom = models.MultiPolygonField(srid=4326)

    def _unicode_(self):
        return self.amodiatair

    def __str__(self):
        return self.amodiatair
