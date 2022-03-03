import json, jwt
from . import models


from django.views     import View
from django.http      import JsonResponse
from django.views.generic import ListView

from products.models  import Product, ProductSize
from users.utils      import login_decorator

class ListView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            name = data.get("name", "")
            description=data.get("description", "")
            thumbnail = data.get("thumbnail", "")
            discount_rate = data.get("discount_rate", "")
                
            Product.objects.create(
                name=name,
                description=description,
                thumbnail=thumbnail,
                discount_rate=discount_rate
            )
            return JsonResponse({"MESSAGE": "List Created!"}, status=201)
        
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)

    def get(self, request):
        products   = Product.objects.filter()
        productsize     = ProductSize.objects.filter()
        results = []
        
        for product in products:            
                product_id = product.id
                results.append(
                    {
                    "id" : product.id,
                    "name" : product.name,
                    "description" : product.description,
                    "thumbnail" : product.thumbnail,
                    "sizes" : product.sizes.all()[0].size,
                    "discount_rate" : product.discount_rate,
                    "price": productsize[product_id].price
                }
            )
        return JsonResponse({"lists" : results}, status = 200)        
    
