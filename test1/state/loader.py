from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import state_results

state_results_mapping = {
    'objectid_1': 'OBJECTID_1',
    'objectid': 'OBJECTID',
    'pau_name': 'PAU_NAME',
    'village': 'VILLAGE',
    'pau_code': 'PAU_CODE',
    'vill_code': 'VILL_CODE',
    'st_name': 'ST_NAME',
    'st_code': 'ST_CODE',
    'loc_name': 'LOC_NAME',
    'loc_code': 'LOC_CODE',
    'au_name': 'AU_NAME',
    'au_code': 'AU_CODE',
    'elec': 'Elec',
    'phone': 'Phone',
    'wc': 'WC',
    'oid_join': 'OID_Join',
    'state': 'State',
    'county': 'County',
    'au': 'AU',
    'pau': 'PAU',
    'm_0_4': 'M_0_4',
    'f_0_4': 'F_0_4',
    'm_5_14': 'M_5_14',
    'f_5_14': 'F_5_14',
    'm_15_24': 'M_15_24',
    'f_15_24': 'F_15_24',
    'm_25_44': 'M_25_44',
    'f_25_44': 'F_25_44',
    'm_45_plus': 'M_45_Plus',
    'f_45_plus': 'F_45_Plus',
    'tot_pop': 'TOT_POP',
    'tot_hhs': 'Tot_HHS',
    'shape_leng': 'Shape_Leng',
    'shape_le_1': 'Shape_Le_1',
    'shape_area': 'Shape_Area',
    'fam': 'Fam',
    'census': 'Census',
    'es1': 'ES1',
    'es2': 'ES2',
    'geom': 'MULTIPOLYGON',
}

def load():
    path = Path(__file__).parent.joinpath('data/b1.shp')
    layer = LayerMapping(state_results,path,state_results_mapping,transform=True,encoding='utf-8')
    layer.save(verbose=True)


