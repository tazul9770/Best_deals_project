from rest_framework import serializers
from decimal import Decimal
from product.models import Product, Category

# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     my_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price')
#     tax_price = serializers.SerializerMethodField(method_name='calculate_tax')
#     # category = CategorySerializer()
#     category = serializers.HyperlinkedRelatedField(
#         queryset = Category.objects.all(),
#         view_name = 'view_specific_category',
#     )

#     def calculate_tax(self, product):
#         return round(product.price * Decimal(1.1), 2)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'stock', 'price', 'category', 'tax_price']

    # category = serializers.HyperlinkedRelatedField(
    #      queryset = Category.objects.all(),
    #      view_name = 'view_specific_category',
    #  )

    tax_price = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product):
         return round(product.price * Decimal(1.1), 2)

    # field validators
    def validate_price(self, price):
        if price <= 0:
            raise serializers.ValidationError("Price could not negative")
        return price