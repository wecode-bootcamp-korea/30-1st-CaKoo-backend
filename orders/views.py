from django.http  import JsonResponse
from django.views import View

from users.utils  import login_decorator
from orders.models import Order

class OrderView(View):
    @login_decorator
    def get(self, request):
        try:
            user   = request.user
            orders = Order.objects.filter(user=user)
            
            # result = [{
            #     'user_name'   : user.name,
            #     'user_phone'  : user.phone_number,
                # 'total_price' : int(sum([cart.product_size.price * cart.quantity for cart in carts])),
            #     'items'       : [{
            #         'product_name' : order.product_size.product.name,
            #         'quantity'     : cart.quantity,
            #         'price'        : int(cart.quantity * cart.product_size.price),
            #         'thumbnail'    : cart.product_size.product.thumbnail,
            #         'size'         : cart.product_size.size.size   
            #     } for cart in orders]
            # }]

            result = [{
                "user_name" : user.name, 
                "data" : [{
                    "order_id" : order.id,
                    "order_number" : order.order_number,
                    "items" : [{
                        "product_id" : order_item.product_size.product.id,
                        "product_name" : order_item.product_size.product.name,
                        "size" : order_item.product_size.size.size,
                        "price" : order_item.product_sie.price
                    }for order_item in order.orderitems.all()]
                }for order in orders]
            }]

            return JsonResponse({"message" : result}, status = 200)
        
        except Order.DoesNotExist:
            return JsonResponse({"message" : "DOES_NOT_EXIST"})