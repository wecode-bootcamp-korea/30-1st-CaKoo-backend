from django.db import models

class Order(models.Model):
    order_number    = models.CharField(unique=True)
    sender_name     = models.CharField(max_length=50)
    address         = models.CharField(max_length=500)
    recipient_name  = models.CharField(max_length=50)
    recipient_phone = models.CharField(max_length=50)
    ordered_at      = models.DateTimeField(auto_now_add=True)
    order_status    = models.ForeignKey("OrderStatus", related_name="orders", on_delete=models.PROTECT)
    user            = models.ForeignKey("users.User", related_name="orders", on_delete=models.PROTECT)
    
    class Meta:
        db_table = "orders"

class OrderStatus(models.Model):
    status = models.CharField(max_length=15)
    
    class Meta:
        db_table = "orderstatus"
        
class OrderItem(models.Model):
    order        = models.ForeignKey("Order", related_name="orderitems", on_delete=models.CASCADE)
    product_size = models.ForeignKey("products.ProductSize", related_name="orderitems", on_delete=models.CASCADE)
    quantity     = models.IntegerField()
    
    class Meta:
        db_table = "orderitems"
        