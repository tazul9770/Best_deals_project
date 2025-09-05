from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializer import ProductSerializer
from django.shortcuts import get_object_or_404
from product.serializer import CategorySerializer
from django.db.models import Count

@api_view()
def view_products(request):
    products = Product.objects.select_related('category').all()
    serializer = ProductSerializer(products, many=True, context={'request':request})
    return Response(serializer.data)

@api_view()
def view_specific_product(request, pk):
    try:
        p = Product.objects.get(pk=pk)
        serializer = ProductSerializer(p)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"message":"Product does not exists"}, status=status.HTTP_404_NOT_FOUND)

@api_view()
def category_view(request):
    category = Category.objects.annotate(product_count = Count('product')).all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

@api_view()
def specific_category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)