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
region = [
    ('Zone avale', 'Zone avale'),
    ('Parc à bois', 'Parc à bois'),
    ('Zone de pêche', 'Zone de pêche'),
]

class Aot(models.Model):
    id_aot = models.IntegerField()
    amodiataire = models.CharField(max_length=50)
    rccm = models.CharField(max_length=50, verbose_name="RCCM")
    niu = models.CharField(max_length=50, verbose_name="NIU")
    bp = models.CharField(max_length=50, verbose_name="BP")
    tel = models.BigIntegerField(default=None, verbose_name="Tel")
    duree_bail = models.IntegerField(default=None, verbose_name="Durée Bail (ans)")
    taux_loyer = models.IntegerField(default=None, verbose_name="Taux loyer (CFA/m²)")
    date_debut = models.DateField(default=None, verbose_name="Date facturation loyer")
    date_fin = models.DateField(default=None, verbose_name="Date expiration loyer")
    date_caution = models.DateField(default=None, verbose_name="Date paiement caution")
    superficie = models.FloatField(default=None, verbose_name="Superficie (m²)")
    montant_caution = models.BigIntegerField(default=None, verbose_name="Montant caution")
    localisation = models.CharField(max_length=50, choices=region, default=None, null=True)
    remarque = models.CharField(max_length=50, default=None, null=True, blank=True)
    statut = models.CharField(max_length=50, choices=color, default='green')
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
    nouvel_ind = models.IntegerField(default=None, verbose_name="Nouvel index")
    ancien_ind = models.IntegerField(default=None, verbose_name="Ancien index")
    coef = models.IntegerField(default=None)
    conso_m3 = models.BigIntegerField(default=None)
    prix_unit = models.BigIntegerField(default=None, verbose_name="Prix unitaire")
    mont_conso = models.BigIntegerField(default=None, verbose_name="Montant consommation")
    entretien = models.BigIntegerField(default=None)
    mont_payer = models.BigIntegerField(default=None, verbose_name="Montant payé")
    amodiataire = models.CharField(max_length=50)
    rccm = models.CharField(max_length=50, verbose_name="RCCM")
    niu = models.CharField(max_length=50, verbose_name="NIU")
    bp = models.CharField(max_length=50, verbose_name="BP")
    tel = models.BigIntegerField(default=None, verbose_name="Tel")
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

class CheminFer(models.Model):
    full_id = models.CharField(max_length=25)
    usage = models.CharField(max_length=20, null=True, blank=True)
    service = models.CharField(max_length=20, null=True, blank=True)
    gauge = models.CharField(max_length=10 ,null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def _unicode_(self):
        return self.full_id

    def __str__(self):
        return self.full_id

class ReseauElec(models.Model):
    full_id = models.CharField(max_length=25)
    highway = models.CharField(max_length=50, null=True, blank=True)
    service = models.CharField(max_length=50, null=True, blank=True)
    oneway = models.CharField(max_length=50, null=True, blank=True)
    surface = models.CharField(max_length=25, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def _unicode_(self):
        return self.full_id

    def __str__(self):
        return self.full_id
