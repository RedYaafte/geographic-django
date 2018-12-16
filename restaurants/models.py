from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.
class Restaurant(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    location = geomodels.PointField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

