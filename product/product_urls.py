from django.urls import path
from product.views import ProductList, SpecificProductView

urlpatterns = [
    path('', ProductList.as_view(), name='view_products'),
    path('<int:pk>/', SpecificProductView.as_view(), name='specific_product')
]
