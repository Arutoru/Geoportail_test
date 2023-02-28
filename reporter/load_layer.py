import os
import csv
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.geos import Point
from .models import Aot, Index


aot_mapping = {
    'id_aot': 'ID_AOT',
    'amodiatair': 'AMODIATAIR',
    'rccm': 'RCCM',
    'niu': 'NIU',
    'bp': 'BP',
    'tel': 'TEL',
    'duree_bail': 'DUREE_BAIL',
    'taux_loyer': 'TAUX_LOYER',
    'sup': 'sup',
    'mont_cauti': 'mont_cauti',
    'date_caut': 'Date_caut',
    'geom': 'MULTIPOLYGON',
}

index_mapping = {
    'objectid': 'OBJECTID',
    'join_count': 'Join_Count',
    'target_fid': 'TARGET_FID',
    'join_fid': 'JOIN_FID',
    'code_tarif': 'code_tarif',
    'compteur': 'compteur',
    'nouvel_ind': 'Nouvel_Ind',
    'ancien_ind': 'Ancien_ind',
    'coef': 'coef',
    'conso_m3': 'Conso_m3',
    'prix_unit': 'prix_unit',
    'mont_conso': 'mont_conso',
    'entretien': 'entretien',
    'mont_payer': 'mont_payer',
    'amodiatair': 'AMODIATAIR',
    'rccm': 'RCCM',
    'niu': 'NIU',
    'bp': 'BP',
    'tel': 'TEL',
    'geom': 'MULTIPOINT',
}

aot_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/AOT.shp'))
index_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/index.shp'))

def runAot(verbose=True):
    lm = LayerMapping(Aot, aot_shp, aot_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runIndex(verbose=True):
    lm = LayerMapping(Index, index_shp, index_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)



# csv_file = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/Bornes.txt'))
# reader = csv.reader(open(csv_file), delimiter='\t')
# def run_borne():
#     for line in reader:
#         try:
#             lng = float(line[2])
#             lat = float(line[3])
#             east = float(line[4])
#             nord = float(line[5])
#             name = line[1].title()
#         except:
#             continue
#         Borne(name = name, east = east, nord = nord, geom=Point(lng, lat)).save()
