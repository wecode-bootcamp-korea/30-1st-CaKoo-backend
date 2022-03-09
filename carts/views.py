import json

from django.http  import JsonResponse
from django.views import View

from users.utils  import login_decorator
from .models      import Cart

class CartView(View):
    @login_decorator
    def get(self, request):
        try:
            user   = request.user
            carts  = Cart.objects.filter(user=user)
            result = []
            cart   = carts

            for cart in carts:
                cart = {
                    "cart_id"       : cart.id,
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
    
    @login_decorator
    def patch(self, request, cart_id):
        try:
            data     = json.loads(request.body)
            quantity = data['quantity']            
            
            cart          = Cart.objects.get(id = cart_id, user = request.user)
            cart.quantity = quantity
            cart.save()
        
            return JsonResponse({"message" : "SUCCESS"}, status = 200)
        
        except Cart.DoesNotExist:
            return JsonResponse({"message" : "INVALID_CART"}, status = 404)
        
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 401)

    @login_decorator
    def delete(self, request, cart_id):
        try:
            cart = Cart.objects.get(id = cart_id, user = request.user)
            cart.delete()

            return JsonResponse({"message":"NO_CONTENT"}, status=204)
        
        except Cart.DoesNotExist:
            return JsonResponse({"message" : "INVALID_CART"}, status = 404)
            