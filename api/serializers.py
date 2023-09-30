from rest_framework import serializers

from product.models import product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = product
        fields = [
            "id",
            "title",
            "content",
            "price",
            "sale_price",
        
        ]