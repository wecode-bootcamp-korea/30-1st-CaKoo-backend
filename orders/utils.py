import string, random, datetime

from .models import Order

def validate_order_number(request):
    string_pool              = string.ascii_letters + string.digits
    number_length            = 2
    back_order_number_string = ""

    for i in range(number_length):
        back_order_number_string += random.choice(string_pool)

    order_number_string = datetime.datetime.today().strftime("%y%m%d") + back_order_number_string
    
    if not Order.objects.filter(order_number = order_number_string).exists():
        return validate_order_number()
    
    request.order_number = order_number_string
    
    return request.order_number

    ##생각 좀 해보자