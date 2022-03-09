from django.http  import JsonResponse
from django.views import View

from users.utils  import login_decorator
from carts.models import Cart

class OrderView(View):
    @login_decorator
    def get(self, request):
        carts = Cart.objects.filter(user = request.user)
        
        result = [{
            'user_name'   : request.user.name,
            'user_phone'  : request.user.phone_number,
            'total_price' : int(sum([cart.product_size.price * cart.quantity for cart in carts])),
            'items'       : [{
                              'product_name' : cart.product_size.product.name,
                              'quantity'     : cart.quantity,
                              'price'        : int(cart.quantity * cart.product_size.price),
                              'thumbnail'    : cart.product_size.product.thumbnail,
                              'size'         : cart.product_size.size.size   
            } for cart in carts]
        }]

        return JsonResponse({"message" : result}, status = 200)