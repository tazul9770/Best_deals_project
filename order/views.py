from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from order.serializer import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer
from order.models import Cart, CartItem

class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        # ei context diye cart id pathano hoitace
        return {'cart_id':self.kwargs['carts_pk']}
    
    # Jodi nijer moto kore filter korte chai, taile ei method override korte hobe
    def get_queryset(self):
        return CartItem.objects.filter(cart_id = self.kwargs['carts_pk'])

