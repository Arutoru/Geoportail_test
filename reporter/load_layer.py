import os
import csv
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.geos import Point
from .models import Region, Borne


region_mapping = {
    'sce_geo': 'SCE_GEO',
    'sce_sem': 'SCE_SEM',
    'date': 'DATE',
    'origine': 'ORIGINE',
    'region': 'REGION',
    'nom': 'NOM',
    'superficie': 'SUPERFICIE',
    'geom': 'MULTIPOLYGON',
}
region_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/502_RGRC_Region_region.shp'))

def run(verbose=True):
    lm = LayerMapping(Region, region_shp, region_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

csv_file = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/Bornes.txt'))
reader = csv.reader(open(csv_file), delimiter='\t')
def run_borne():
    for line in reader:
        try:
            lng = float(line[2])
            lat = float(line[3])
            east = float(line[4])
            nord = float(line[5])
            name = line[1].title()
        except:
            continue
        Borne(name = name, east = east, nord = nord, geom=Point(lng, lat)).save()
