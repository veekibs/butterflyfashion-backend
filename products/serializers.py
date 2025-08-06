# Import the necessary tools from Django Rest Framework + models file
from rest_framework import serializers
from .models import Product

# Define serializer for the Product model
class ProductSerializer(serializers.ModelSerializer):
    # The Meta class tells the serializer which model it's for + which fields to include
    class Meta:
        model = Product
        # '__all__' is a shortcut to include all the fields defined in the Product model
        fields = '__all__'