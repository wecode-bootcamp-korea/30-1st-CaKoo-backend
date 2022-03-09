import json, uuid

from django.http   import JsonResponse
from django.views  import View
from django.db     import transaction

from users.utils   import login_decorator
from carts.models  import Cart
from orders.models import Order,OrderItem, OrderStatus

class OrderView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            
            carts        = Cart.objects.filter(user=user)
            uuid_        = uuid.uuid4() 
            order_status = OrderStatus.objects.get(status="Confirmed") 

            with transaction.atomic():
                order = Order.objects.create(
                        user            = user, 
                        sender_name     = user.name,
                        order_number    = uuid_,
                        order_status    = order_status,
                        address         = data["address"],
                        recipient_name  = data["recipient_name"],
                        recipient_phone = data["recipient_phone"],
                    )
            
            order_items = [
                OrderItem(
                    order        = order,
                    product_size = cart.product_size,
                    quantity     = cart.quantity
                ) for cart in carts
            ]     
            OrderItem.objects.bulk_create(order_items)

            Cart.objects.filter(user=user).delete()
            return JsonResponse({"message" : "SUCCESS"}, status=201)

        except KeyError as e:
            return JsonResponse({"message" : getattr(e, 'message', str(e))}, status=401)
        
        

            
