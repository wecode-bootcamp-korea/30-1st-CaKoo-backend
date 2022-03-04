import json, jwt

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q, F, Count , Max , Window

from products.models  import Product, ProductSize

class ProductsView(View):
    def get(self, request): 
        try:
            ordering = request.GET.get('ordering', None)
            filter_set = {}            
                
            products = Product.objects.filter(**filter_set)
            
            if ordering == 'recent':
                products = Product.objects.order_by('-created_at')
                
            results = [{
                "id"            : product.id,
                "name"          : product.name,
                "description"   : product.description,
                "thumbnail"     : product.thumbnail,
                "sizes"         : product.sizes.all()[0].size,
                "discount_rate" : float(product.discount_rate),
                "price"         : int(ProductSize.objects.filter(product=product).first().price) * float(product.discount_rate)
                } for product in products]
            
            if ordering == 'min_price':
                results = sorted(results, key=lambda product: product['price'])
            
            if ordering == 'max_price':
                results = sorted(results, key=lambda product: product['price'], reverse=True)
   
            
            return JsonResponse({"lists" : results}, status = 200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
                