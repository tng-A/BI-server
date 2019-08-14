""" Product serializers"""

from rest_framework import serializers

from src.api.models.product import Product
from src.api.serializers.department import DepartmentSerializer

class ProductSerializer(serializers.ModelSerializer):
    """ Product model serializer"""

    department = DepartmentSerializer(read_only=True)

    class Meta:
        """ Meta options"""
        
        model = Product
        fields = ['name', 'description', 'department']
