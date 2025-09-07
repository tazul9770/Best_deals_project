from rest_framework import serializers
from decimal import Decimal
from product.models import Product, Category
from order.models import Review

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']

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
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'comment']
    
    def create(self, validated_data):
        product_id = self.context['product_id']
        review = Review.objects.create(product_id=product_id, **validated_data)
        return review