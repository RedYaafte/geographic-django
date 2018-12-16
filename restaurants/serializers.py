from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    distance = serializers.DecimalField(
        source='distance.m',
        max_digits=10,
        decimal_places=2,
        required=False,
        read_only=True
    )
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'lat', 'lng', 'location', 'distance')
        # read_only_fields = ['location']