import os
import csv
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.geos import Point
from .models import Aot


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

aot_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/AOT.shp'))

def run(verbose=True):
    lm = LayerMapping(Aot, aot_shp, aot_mapping, transform=False, encoding='iso-8859-1')
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
