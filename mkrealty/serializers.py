from rest_framework import serializers
from .models import Realty


class RealtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Realty
        fields = ['id', 'name', 'type', 'price', 'location', 'info', 'status']