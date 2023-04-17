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
    amodiataire = models.CharField(max_length=50)
    rccm = models.CharField(max_length=50)
    niu = models.CharField(max_length=50)
    bp = models.CharField(max_length=50)
    tel = models.BigIntegerField(default=None)
    duree_bail = models.IntegerField(default=None)
    taux_loyer = models.IntegerField(default=None)
    date_debut = models.DateField(default=None)
    date_fin = models.DateField(default=None)
    date_caution = models.DateField(default=None)
    superficie = models.FloatField(default=None)
    montant_caution = models.BigIntegerField(default=None)
    statut = models.CharField(max_length=50, choices=color, default='green')
    remarque = models.CharField(max_length=50, default='R.A.S.')
    geom = models.MultiPolygonField(srid=4326)


    def _unicode_(self):
        return self.amodiataire

    def __str__(self):
        return self.amodiataire

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
    code_tarif = models.IntegerField(default=None)
    compteur = models.IntegerField(default=None)
    nouvel_ind = models.IntegerField(default=None)
    ancien_ind = models.IntegerField(default=None)
    coef = models.IntegerField(default=None)
    conso_m3 = models.BigIntegerField(default=None)
    prix_unit = models.BigIntegerField(default=None)
    mont_conso = models.BigIntegerField(default=None)
    entretien = models.BigIntegerField(default=None)
    mont_payer = models.BigIntegerField(default=None)
    amodiataire = models.CharField(max_length=50)
    rccm = models.CharField(max_length=50)
    niu = models.CharField(max_length=50)
    bp = models.CharField(max_length=50)
    tel = models.BigIntegerField()
    geom = models.MultiPointField(srid=4326)

    def _unicode_(self):
        return self.amodiataire

    def __str__(self):
        return self.amodiataire


class Route(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20)
    nom_rue = models.CharField(max_length=20)
    numero_rue = models.CharField(max_length=10)
    geom = models.MultiLineStringField(srid=4326)

    def _unicode_(self):
        return self.nom_rue

    def __str__(self):
        return self.nom_rue
