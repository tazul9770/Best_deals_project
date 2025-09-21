from order.models import Cart, Order, OrderItem
from django.db import transaction
from rest_framework.exceptions import PermissionDenied, ValidationError

class OrderService:
    @staticmethod
    def create_order(user_id, cart_id):
        try:
            with transaction.atomic():
                cart = Cart.objects.get(pk=cart_id)
                print(cart)
                cart_items = cart.items.select_related('product').all()
                total_price = 0
                for item in cart_items: 
                    total_price += item.quantity * item.product.price

                order = Order.objects.create(user_id=user_id, total_price=total_price)

                order_items = [
                    OrderItem(
                        order=order,
                        product=item.product,
                        quantity=item.quantity,
                        price=item.product.price,
                        total_price=item.quantity * item.product.price
                    )
                    for item in cart_items
                ]
                OrderItem.objects.bulk_create(order_items)
                cart.delete() 
                print(cart)
                return order

        except Cart.DoesNotExist:
            print(f"Cart with id {cart_id} not found")
            return None
        except Exception as e:
            print(f"Error while creating order: {e}")
            raise e 
        
    @staticmethod
    def cancel(order, user):
        if user.is_staff:
            order.status = Order.CANCELED
            order.save()
            return order
        if order.user != user:
            raise PermissionDenied({'message':"You can cancel just your own order, ok !"})
        if order.status == Order.DELIVERED:
            raise ValidationError({'message':"You cannot delete order because this order is already placed !"})
        order.status = Order.CANCELED
        order.save()
        return order
