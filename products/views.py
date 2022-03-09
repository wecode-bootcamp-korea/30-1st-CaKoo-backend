from django.http      import JsonResponse
from django.views     import View
from django.db.models import Min, Q

from products.models  import Product

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product          = Product.objects.annotate(base_price=Min("productsizes__price")).get(id = product_id)
            product_urls     = [image.url for image in product.productimages.all()]
            information_urls = [information_image.url for information_image in product.informationimages.all()]
            
            sizes = [{
                'size_id' : product_size.size.id,
                'size'    : product_size.size.size,
                'price'   : product_size.price
            } for product_size in product.productsizes.all()]
        
            result = {
                'description'        : product.description,
                'name'               : product.name,
                'base_price'         : product.base_price,
                'sizes'              : sizes,
                'discount_rate'      : product.discount_rate,
                'product_images'     : product_urls,
                'information_images' : information_urls
            }
            
            return JsonResponse({"message" : result}, status = 200)

        except Product.DoesNotExist:
            return JsonResponse({"message" : "INVALID_PRODUCT"}, status = 404)

class ProductsView(View):
    def get(self, request): 
        try:
            sort     = request.GET.get('sort', "recent")
            size     = request.GET.get('size', 0)
            offset   = int(request.GET.get('offset', 0))
            limit    = int(request.GET.get('limit', 8))
            
            q = Q()
                
            if size:
                size = size.split(',')
                q &= Q(sizes__in=size)
            
            sort_set = {
                'recent'    : '-created_at',
                'old'       : 'created_at',
                'expensive' : '-base_price',
                'cheap'     : 'base_price' 
            } 
                      
            products = Product.objects.annotate(base_price=Min('productsizes__price'))
            
            results = [{
                "id"             : product.id,
                "name"           : product.name,
                "description"    : product.description,
                "thumbnail"      : product.thumbnail,
                "sizes"          : [size.size for size in product.sizes.all().order_by('id')],
                "discount_rate"  : float(product.discount_rate),
                "price"          : int(product.base_price), 
                "discount_price" : int(product.base_price * product.discount_rate)
            } for product in products.filter(q).order_by(sort_set[sort])[offset:offset+limit]]
                

            return JsonResponse({"lists" : results}, status = 200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)