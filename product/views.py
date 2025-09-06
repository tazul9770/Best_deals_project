from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializer import ProductSerializer
from django.shortcuts import get_object_or_404
from product.serializer import CategorySerializer
from django.db.models import Count

@api_view(['GEt','POST'])
def view_products(request):
    if request.method == 'GET':
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET', 'PUT', 'DELETE'])
def view_specific_product(request, pk):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    if request.method == 'PUT':
       product = get_object_or_404(Product, pk=pk)
       serializer = ProductSerializer(product, data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data)
    if request.method == 'DELETE':
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     

@api_view(['GET', 'POST'])
def category_view(request):
    if request.method == 'GET':
        category = Category.objects.annotate(product_count = Count('product')).all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    

@api_view()
def specific_category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)