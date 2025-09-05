from django.urls import path
from product.views import category_view, specific_category_view

urlpatterns = [
    path('', category_view),
    path('<int:pk>/', specific_category_view, name='view_specific_category')
]