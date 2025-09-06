from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializer import ProductSerializer
from django.shortcuts import get_object_or_404
from product.serializer import CategorySerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
        
class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

class SpecificProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
        
class CategoryList(ListCreateAPIView):
    queryset = Category.objects.annotate(product_count=Count('product')).all()
    serializer_class = CategorySerializer

class SpecificCategoryView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.prefetch_related('product').all()
    serializer_class = CategorySerializer