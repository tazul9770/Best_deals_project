from django.contrib import admin
from order.models import Cart, CartItem, Review, Order, OrderItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    
admin.site.register(CartItem)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status']

admin.site.register(OrderItem)

admin.site.register(Review)
