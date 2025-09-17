from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from order.models import Review
from product.serializer import ProductSerializer, CategorySerializer, ReviewSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from product.pagination import CustomPagination
from product.filters import ProductFilter
from api.permissions import IsAdminOrReadOnly
from product.permissions import IsReviewAuthorOrReadOnly
from rest_framework.permissions import DjangoModelPermissions
        
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['category_id', 'price']
    pagination_class = CustomPagination
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price']
    permission_classes = [IsAdminOrReadOnly]

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('product')).all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {
            'product_id':self.kwargs['product_pk'],
        }