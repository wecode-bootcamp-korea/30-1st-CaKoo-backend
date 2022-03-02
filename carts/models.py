from django.db import models

class Cart(models.Model):
    quantity     = models.IntegerField()
    user         = models.ForeignKey("users.User", related_name="carts", on_delete=models.CASCADE)
    product_size = models.ForeignKey("products.ProductSize", related_name="carts", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "carts" 