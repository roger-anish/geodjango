import os
from django.contrib.gis.utils import LayerMapping
from .models import districts 

districts_mapping = {
    'district': 'DISTRICT',
    'count': 'COUNT',
    'var_vdc_co': 'VAR_VDC_CO',
    'z_code': 'Z_CODE',
    'zone': 'ZONE',
    'area': 'AREA',
    'division': 'DIVISION',
    'geom': 'MULTIPOLYGON',
}

districts_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','District.shp'),)  #for fetch

def run(verbose= True):
    lm= LayerMapping(districts, districts_shp, districts_mapping, transform=False, encoding='utf-8')
    lm.save(strict=True,verbose=verbose)