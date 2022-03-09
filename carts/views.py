import json

from django.http    import JsonResponse
from django.views   import View

from users.utils     import login_decorator
from users.models    import User
from products.models import ProductSize
from .models         import Cart

class CartView(View):
    @login_decorator
    def get(self, request):
        try:
            user   = request.user
            carts  = Cart.objects.filter(user=user)
            result = []

            for cart in carts:
                cart = {
                    "cart_id"       : cart.id,
                    "product_name"  : cart.product_size.product.name,
                    "product_size"  : cart.product_size.size.size,
                    "product_price" : int(cart.product_size.price * cart.product_size.product.discount_rate),
                    "cart_quantity" : cart.quantity,
                    "discount_rate" : float(cart.product_size.product.discount_rate),
                    "thumbnail"     : cart.product_size.product.thumbnail
                }
                result.append(cart)

            return JsonResponse({"message" : result}, status = 200)
        
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 401)

        except Cart.DoesNotExist:
            return JsonResponse({"message" : "CART_NOT_EXIST"}, status = 404)

    @login_decorator
    def post(self, request):        
        try:
            data_list = json.loads(request.body)
            user      = request.user
            
            for data in data_list:
                size_id      = data["size_id"]
                product_id   = data["product_id"]
                quantity     = data["quantity"]
                product_size = ProductSize.objects.get(product_id=product_id, size_id=size_id)

                if quantity < 1:
                    return JsonResponse({"message" : "INVALID ERROR"}, status = 400)

                cart, created = Cart.objects.get_or_create(
                    user_id       = user.id,
                    product_size  = product_size,
                    defaults      = {"quantity": quantity}
                )

                if not created:
                    cart.quantity += quantity
                    cart.save()
                    return JsonResponse({"message" : "SUCCESS"}, status = 200)

            return JsonResponse({"message" : "SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse({"message" : "KEYERROR"}, status = 401)

        except Cart.DoesNotExist:
            return JsonResponse({"message" : 'CART_NOT_EXIST'}, status = 404)
    
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
