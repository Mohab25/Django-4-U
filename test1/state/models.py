from django.contrib.gis.db import models 

class state_results(models.Model):
    objectid_1 = models.BigIntegerField()
    objectid = models.BigIntegerField()
    pau_name = models.CharField(max_length=254)
    village = models.CharField(max_length=254)
    pau_code = models.CharField(max_length=254)
    vill_code = models.CharField(max_length=254)
    st_name = models.CharField(max_length=254)
    st_code = models.FloatField()
    loc_name = models.CharField(max_length=254)
    loc_code = models.CharField(max_length=254)
    au_name = models.CharField(max_length=254)
    au_code = models.CharField(max_length=254)
    elec = models.FloatField()
    phone = models.FloatField()
    wc = models.FloatField()
    oid_join = models.CharField(max_length=254)
    state = models.CharField(max_length=254)
    county = models.CharField(max_length=254)
    au = models.CharField(max_length=254)
    pau = models.CharField(max_length=254)
    m_0_4 = models.BigIntegerField()
    f_0_4 = models.BigIntegerField()
    m_5_14 = models.BigIntegerField()
    f_5_14 = models.BigIntegerField()
    m_15_24 = models.BigIntegerField()
    f_15_24 = models.BigIntegerField()
    m_25_44 = models.BigIntegerField()
    f_25_44 = models.BigIntegerField()
    m_45_plus = models.BigIntegerField()
    f_45_plus = models.BigIntegerField()
    tot_pop = models.BigIntegerField()
    tot_hhs = models.BigIntegerField()
    shape_leng = models.FloatField()
    shape_le_1 = models.FloatField()
    shape_area = models.FloatField()
    fam = models.CharField(max_length=254)
    census = models.BigIntegerField()
    es1 = models.BigIntegerField()
    es2 = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        ordering=['objectid']
    
    def __str__(self):
        return str.pau_name