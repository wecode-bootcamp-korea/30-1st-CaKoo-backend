import string, random, datetime


def validate_order_number():
    string_pool = string.ascii_letters + string.digits
    number_length  = 2
    back_order_number_string  = ""

    for i in range(number_length):
        back_order_number_string += random.choice(string_pool)

    order_number_string = datetime.datetime.today().strftime("%y%m%d") + back_order_number_string
    
    return order_number_string