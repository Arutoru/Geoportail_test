from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.geos import Point
from django.utils import timezone
from django.db.models import Manager as GeoManager
import os

color = [
    ('green', 'Bon'),
    ('orange', 'Intermédiaire'),
    ('red', 'Critique'),
]

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
    statut = models.CharField(max_length=50, choices=color, default='green')
    remarque = models.CharField(max_length=50, default='R.A.S.')

    def _unicode_(self):
        return self.amodiatair

    def __str__(self):
        return self.amodiatair

    # def approve_facture(self):
    #     return self.comments.filter(approved_facture=True)
    #
    # def get_absolute_url(self):
    #     return reverse("aot_detail",kwargs={'pk':self.pk})

# class Facture(object):
#     aot = models.ForeignKey('reporter.Aot', related_name='factures' ,on_delete=models.CASCADE)
#     mont_facture = models.BigIntegerField()

class Index(models.Model):
    objectid = models.IntegerField()
    join_count = models.IntegerField()
    target_fid = models.IntegerField()
    join_fid = models.IntegerField()
    code_tarif = models.IntegerField()
    compteur = models.IntegerField()
    nouvel_ind = models.IntegerField()
    ancien_ind = models.IntegerField()
    coef = models.IntegerField()
    conso_m3 = models.BigIntegerField()
    prix_unit = models.BigIntegerField()
    mont_conso = models.BigIntegerField()
    entretien = models.BigIntegerField()
    mont_payer = models.BigIntegerField()
    amodiatair = models.CharField(max_length=50)
    rccm = models.CharField(max_length=50)
    niu = models.CharField(max_length=50)
    bp = models.CharField(max_length=50)
    tel = models.BigIntegerField()
    geom = models.MultiPointField(srid=32632)

    def _unicode_(self):
        return self.amodiatair

    def __str__(self):
        return self.amodiatair
