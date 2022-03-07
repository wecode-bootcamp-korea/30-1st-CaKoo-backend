from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from products.models  import Product, ProductSize

class ProductsView(View):
    def get(self, request): 
        try:
            ordering = request.GET.get('ordering', None)
            sort     = request.GET.get('sort', "id")
            size     = request.GET.get('size', 0)
            offset     = int(request.GET.get('offset', 0))
            limit    = int(request.GET.get('limit', 8))
            
            q = Q()
                
            if size:
                size = size.split(',')
                q &= Q(sizes__in=size)
            
            sort_set = {
                "id" : "id",
                'recent': '-created_at',
                'old': 'created_at',
            } 
                      
            results = [{
                "id"             : product.id,
                "name"           : product.name,
                "description"    : product.description,
                "thumbnail"      : product.thumbnail,
                "sizes"          : ProductSize.objects.filter(product=product).first().size.size,
                "discount_rate"  : float(product.discount_rate),
                "price"          : int(ProductSize.objects.filter(product=product).first().price), 
                "discount_price" : int(ProductSize.objects.filter(product=product).first().price) * float(product.discount_rate)
                #"all_sizes"      : [ProductSize.objects.filter(product=product).first().size.size for in]
                } for product in Product.objects.filter(q).distinct().order_by(sort_set[sort])[offset:offset+limit]]
                
            if ordering == 'min_price':
                results = sorted(results, key=lambda product: product['discount_price'])
            
            if ordering == 'max_price':
                results = sorted(results, key=lambda product: product['discount_price'], reverse=True)
   
            
            return JsonResponse({"lists" : results}, status = 200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
