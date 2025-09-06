from django.urls import path
from product.views import CategoryList, SpecificCategoryView

urlpatterns = [
    path('', CategoryList.as_view(), name='category_view'),
    path('<int:pk>/', SpecificCategoryView.as_view(), name='view_specific_category')
]