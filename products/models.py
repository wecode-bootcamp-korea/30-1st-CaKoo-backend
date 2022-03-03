from django.db import models

class Product(models.Model):
    name         = models.CharField(max_length=50)
    description  = models.EmailField(max_length=100)
    thumbnail    = models.CharField(max_length=2000)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    sizes        = models.ManyToManyField("Size", related_name="products", through="ProductSize", through_fields=("product", "size"))
    discout_rate = models.DecimalField(max_digits=3, decimal_places=2) 
    
    class Meta:
        db_table = "products"

class ProductSize(models.Model):
    price   = models.DecimalField(max_digits=10, decimal_places=2)    
    product = models.ForeignKey("Product",related_name="productsizes",on_delete=models.CASCADE)
    size    = models.ForeignKey("Size", related_name="productsizes", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "product_sizes"
        
class Size(models.Model):
    size = models.CharField(max_length=20)
    
    class Meta:
        db_table = "sizes"
        
class ProductImage(models.Model):
    sequence = models.IntegerField()
    url      = models.CharField(max_length=2000)
    product  = models.ForeignKey("Product", related_name="productimages", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "product_images"
        
class InformationImage(models.Model):
    sequence = models.IntegerField()
    url      = models.CharField(max_length=2000)
    product  = models.ForeignKey("Product", related_name="informationimages", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "information_images"