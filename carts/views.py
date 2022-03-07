import json

from django.http    import JsonResponse
from django.views   import View
from users.utils    import login_decorator
from users.models   import User
from .models        import Cart

class CartView(View):
    @login_decorator
    def get(self, request):
        try:
            user  = request.user
            carts = Cart.objects.filter(user=user)
            result = []
            cart = carts

            for cart in carts:
                cart = {
                    "cart_id'"      : cart.id,
                    "product_name"  : cart.product_size.product.name,
                    "product_size"  : cart.product_size.size.size,
                    "product_price" : cart.product_size.price,
                    "cart_quantity" : cart.quantity
                }
                result.append(cart)

            return JsonResponse({"message" : result}, status = 200)
        
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 401)

        except Cart.DoesNotExist:
            return JsonResponse({"message" : "CART_NOT_EXIST"}, status = 404)
