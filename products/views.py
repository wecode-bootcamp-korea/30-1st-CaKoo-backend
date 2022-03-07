from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q, F

from products.models  import Product, ProductSize

class ProductsView(View):
    def get(self, request): 
        try:
            sort     = request.GET.get('sort', "id")
            size     = request.GET.get('size', 0)
            offset   = int(request.GET.get('offset', 0))
            limit    = int(request.GET.get('limit', 8))
            
            q = Q()
                
            if size:
                size = size.split(',')
                q &= Q(sizes__in=size)
            
            products = Product.objects.annotate(price=F('productsizes__price'))
                   
            sort_set = {
                'id'        : 'id',
                'recent'    : '-created_at',
                'old'       : 'created_at',
                'expensive' : '-price',
                'cheap'     : 'price' 
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
                } for product in products.filter(q).distinct().order_by(sort_set[sort])[offset:offset+limit]]
                

            return JsonResponse({"lists" : results}, status = 200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)