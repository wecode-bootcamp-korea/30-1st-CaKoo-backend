import json, uuid
from tkinter.messagebox import CANCEL
from enum import Enum

from django.http   import JsonResponse
from django.views  import View
from django.db     import transaction

from users.utils   import login_decorator
from carts.models  import Cart
from orders.models import Order,OrderItem, OrderStatus

class OrderStatus(Enum):
    CONFIRMED = 1  
    CANCELED  = 2
    PENDING   = 3

class OrderView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            
            cart_ids     = data["cart_ids"]
            carts        = Cart.objects.filter(user=user, id__in=cart_ids)
            order_status = OrderStatus.objects.get(status=OrderStatus.CONFIRMED.value) 

            with transaction.atomic():
                order = Order.objects.create(
                        user            = user, 
                        sender_name     = user.name,
                        order_number    = uuid.uuid4(),
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
                    
                
            carts.delete()
            return JsonResponse({"message" : "SUCCESS"}, status=201)

        except transaction.TransactionManagementError:
            return JsonResponse({'message':'TransactionManagementError'}, status=400)  
        except KeyError:
            return JsonResponse({"message" : "KEYERROR"}, status=400)
        
