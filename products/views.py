import json, jwt

from django.views     import View
from django.http      import JsonResponse

from products.models  import Product, ProductSize

class ProductsView(View):
    def get(self, request): 
        products    = Product.objects.all()     
        # product = [product for product in products]
                   
        results = [{
            "id"            : product.id,
            "name"          : product.name,
            "description"   : product.description,
            "thumbnail"     : product.thumbnail,
            "sizes"         : product.sizes.all()[0].size,
            "discount_rate" : product.discount_rate,
            "price"         : ProductSize.objects.filter(product=product).first().price
            } for product in products]
        
                
        return JsonResponse({"lists" : results}, status = 200)
                
