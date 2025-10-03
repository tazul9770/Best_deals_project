from rest_framework import serializers
from decimal import Decimal
from product.models import Product, Category, ProductImage
from order.models import Review
from django.contrib.auth import get_user_model

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']

class ProductImgSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = ProductImage
        fields = ['id','image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImgSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'stock', 'price', 'category', 'tax_price', 'images']

    tax_price = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product):
         return round(product.price * Decimal(1.1), 2)

    # field validators
    def validate_price(self, price):
        if price <= 0:
            raise serializers.ValidationError("Price could not negative")
        return price
    
class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')
    class Meta:
        model = get_user_model()
        fields = ['id', 'name']

    def get_name(self, obj):
        return obj.get_full_name()
    
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name='get_user')
    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'ratings', 'comment']
        read_only_fields = ['user', 'product']

    def get_user(self, obj):
        return SimpleUserSerializer(obj.user).data
    
    def create(self, validated_data):
        product_id = self.context['product_id']
        review = Review.objects.create(product_id=product_id, **validated_data)
        return review