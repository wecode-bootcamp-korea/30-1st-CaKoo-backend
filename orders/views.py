import json

from django.http  import JsonResponse
from django.views import View

from users.utils  import login_decorator
from carts.models import Cart

class OrderView(View):
    @login_decorator
    def get(self, request):
        carts = Cart.objects.filter(user = request.user)
        result = [{
            'name' : cart.product_size.product.name,
            'quantity' : cart.quantity,
            'price' : cart.quantity * cart.product_size.price,
            'thumnail' : cart.product_size.product.thumbnail,
            'user_name' : cart.user.name,
            'user_phone' : cart.user.phone_number
        } for cart in carts]

        return JsonResponse({"message" : result}, status = 200)

    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        sender_name = data['sender_name']
        recipient_name = data['recipient_name']
        recipient_phone = data['recipient_phone']
        address = data['address']

