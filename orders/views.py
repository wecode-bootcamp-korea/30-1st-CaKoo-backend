import json

from django.http  import JsonResponse
from django.views import View

from users.utils  import login_decorator
from carts.models import Cart
from .models      import Order, OrderItem, OrderStatus

class OrderView(View):
    @login_decorator
    def get(self, request):
        result = [{
            'name'       : cart.product_size.product.name,
            'quantity'   : cart.quantity,
            'price'      : cart.quantity * cart.product_size.price,
            'thumnail'   : cart.product_size.product.thumbnail,
            'user_name'  : cart.user.name,
            'user_phone' : cart.user.phone_number
        } for cart in Cart.objects.filter(user = request.user)]

        return JsonResponse({"message" : result}, status = 200)

    @login_decorator
    def post(self, request):
        try:
            data            = json.loads(request.body)
            sender_name     = data['sender_name']
            recipient_name  = data['recipient_name']
            recipient_phone = data['recipient_phone']
            address         = data['address']

            for cart in Cart.objects.filter(user = request.user):
                OrderItem.objects.create(product_size = cart.product_size, quantity = cart.quantity)
            
            order = Order.objects.create(sender_name = sender_name, address = address,\
                                        recipient_name = recipient_name, recipient_phone = recipient_phone,\
                                        user = request.user)

            OrderItem.objects.update(order = order)

            order_number = order.ordered_at.strftime("%y%m%d") + order.