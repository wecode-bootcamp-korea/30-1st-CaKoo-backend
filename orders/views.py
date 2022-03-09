from django.http  import JsonResponse
from django.views import View

from users.utils  import login_decorator
from carts.models import Cart

class OrderView(View):
    @login_decorator
    def get(self, request):
        carts = Cart.objects.filter(user = request.user)
        
        result = [{
            'name'       : cart.product_size.product.name,
            'quantity'   : cart.quantity,
            'price'      : int(cart.quantity * cart.product_size.price),
            'thumnail'   : cart.product_size.product.thumbnail,
            'user_name'  : cart.user.name,
            'user_phone' : cart.user.phone_number
        } for cart in carts]

        result.append({'total_price' : int(sum([cart.product_size.price * cart.quantity for cart in carts]))})

        return JsonResponse({"message" : result}, status = 200)