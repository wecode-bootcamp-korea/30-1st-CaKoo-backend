import json
import uuid

from django.http   import JsonResponse
from django.views  import View
from django.db     import transaction

from users.utils   import login_decorator
from carts.models  import Cart
from orders.models import Order,OrderItem, OrderStatus

class OrderView(View):
    @login_decorator
    @transaction.atomic
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            
            cart_id      = data["cart_id"]
            carts        = Cart.objects.filter(user=user, id=cart_id)
            uuid_        = uuid.uuid4() 
            order_status = OrderStatus.objects.get(status="Confirmed") 

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
                    order        =  order,
                    product_size = cart.product_size,
                    quantity     = cart.quantity
                ) for cart in carts
            ]     
            OrderItem.objects.bulk_create(order_items)

            Cart.objects.filter(user=user).delete()
            return JsonResponse({"message" : "SUCCESS"}, status=201)

        except KeyError as e:
            return JsonResponse({"message" : getattr(e, 'message', str(e))}, status=401)
        
        
    @login_decorator
    def get(self, request):
        try:
            orders = Order.objects.filter(user= request.user)
            
            result = [{
                'order_number'    : order.order_number,
                'order_status'    : order.order_status.status,
                'sender_name'     : order.sender_name,
                'address'         : order.address,
                'recipient_name'  : order.recipient_name,
                'recipient_phone' : order.recipient_phone,
                'user'            : order.user.name,
                'items' : 
                    [{
                        'product_name' : order_item.product_size.product.name,
                        'size'         : order_item.product_size.size.size,
                        'quantity'     : order_item.quantity,
                        'total_price'  : int(order_item.quantity * order_item.product_size.price \
                                             * order_item.product_size.product.discount_rate),
                        'thumbnail'    : order_item.product_size.product.thumbnail,
                        } for order_item in OrderItem.objects.filter(order=order)
                    ]}for order in orders]
            
            return JsonResponse({'message': result}, status=200)

            
        except Order.DoesNotExist:
            return JsonResponse({"message":"Order Does Not Exist"}, status=400)

            
            
