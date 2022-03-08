from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q, Min

from products.models  import Product, ProductSize

class ProductsView(View):
    def get(self, request):

        """
        목적: 데이터베이스에서 제품들의 정보를 가져오는거 
        -> Product.objects.all()

        1. filter
            1-1. 조건1
            1-2. 조건2
        2. sorting
            2-1 sort_set
        3. pagination
            3-1. offset과 limit


        구조

        1. 프론트로부터 받은 조건들 정리
        2. 조건을 가지고 filter 요소를 만듦
        3. sorting 조건 
        4. 데이터 가공
        5. 응답
        """
        try:
            #1. 프론트로부터 받은 조건들 정리
            #:8000/products?sort='recent'&size=0&offset=8
            """
            request.GET = {
                "sort" : "resent",
                "size" : "0",
                "offset" : "8"
            }
            """
            sort   = request.GET.get('sort', "recent")
            size   = request.GET.get('size', 0)
            offset = int(request.GET.get('offset', 0))
            limit  = int(request.GET.get('limit', 8))
            
            #2. 조건들 가지고 filter 요소 만듦
            q = Q()
                
            if size:
                size = size.split(',')
                q &= Q(sizes__in=size)
            
            #3. sort_set
            sort_set = {
                'recent'    : '-created_at',
                'old'       : 'created_at',
                'expensive' : '-base_price',
                'cheap'     : 'base_price' 
            } 

            # 데이터 가공
            products = Product.objects.annotate(base_price=Min('productsizes__price'))
                      
            results = [{
                "id"             : product.id,
                "name"           : product.name,
                "description"    : product.description,
                "thumbnail"      : product.thumbnail,
                "sizes"          : [size.size for size in product.sizes.all()],
                "discount_rate"  : float(product.discount_rate),
                "price"          : int(product.base_price), 
                "discount_price" : int(product.base_price * product.discount_rate)
            } for product in products.filter(q).order_by(sort_set[sort])[offset:offset+limit]]
                
            return JsonResponse({"results" : results}, status = 200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)