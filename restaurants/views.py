from django.shortcuts import render
from rest_framework import viewsets
from .models import Restaurant
from .serializers import RestaurantSerializer

from django.contrib.gis.db.models.functions import Distance, Length
from django.contrib.gis.geos import GEOSGeometry

# OpenCage Geocoder
from opencage.geocoder import OpenCageGeocode
from pprint import pprint

# Ver si funciona sin geocoder
import geocoder

import math

# Pasar Key a settings.py
key = '2ca3979597164bcea9e48f649a297ddc'
geocoder = OpenCageGeocode(key)

class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        latitude = self.request.query_params.get('lat', None)
        longitude = self.request.query_params.get('lgn', None)
        radius = self.request.query_params.get('radius', None)

        if latitude and longitude:
            ptn = GEOSGeometry('POINT(' + str(longitude) + ' ' + str(latitude) + ')', srid=4326)
            qs = qs.annotate(distance=Distance('location', ptn)).order_by('distance')
            area = math.pi * (float(radius)) **2
            print(area)

            # for qs in qs.all():
            #     if area > 50:
            #         print('hola mundo')
        
        return qs

    # def perform_create(self, serializer):
    #     address = serializer.initial_data['address']
    #     results = geocoder.geocode(address)
    #     longitude = results[0]['geometry']['lng']
    #     latitude  = results[0]['geometry']['lat']
    #     # print(u'%f;%f;%s' % (latitude, longitude, address))
    #     pnt = 'POINT(' + str(longitude) + ' ' + str(latitude) + ')'
    #     serializer.save(location=pnt)

    # def perform_create(self, serializer):
    #     address = serializer.initial_data['address']
    #     g = geocoder.google(address)
    #     print(g)
    #     latitude = g.LatLng[0]
    #     longitude = g.LatLng[1]
    #     pnt = 'POINT(' + str(longitude) + ' ' + str(latitude) + ')'
    #     serializer.save(location=pnt)