from django.urls import path
from product.views import view_specific_product, view_products

urlpatterns = [
    path('', view_products),
    path('<int:pk>/', view_specific_product)
]
