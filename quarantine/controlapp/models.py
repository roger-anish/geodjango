from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=20)
    #location = models.PointField(srid=4326)    #spatial
    geom= models.PointField(srid=4326)
    objects= GeoManager()

    def __unicode__(self):                #constructor
        return self.name

    class Meta:
        verbose_name_plural=" Incidences"

class districts(models.Model):
    district = models.CharField(max_length=18)
    count = models.FloatField()
    var_vdc_co = models.FloatField()
    z_code = models.BigIntegerField()
    zone = models.CharField(max_length=15)
    area = models.CharField(max_length=25)
    division = models.CharField(max_length=20)
    geom = models.MultiPolygonField(srid=4326)
    #objects= models.Manager()                    #error in serialize object doesnot exit in class

    def __str__(self):
        return self.district   #instance of the class districts has no 'districts' member

    class Meta:
        verbose_name_plural=" districts"


