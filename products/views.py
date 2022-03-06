from django.http      import JsonResponse
from django.views     import View

from products.models  import Product

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product            = Product.objects.get(id = product_id)
            product_sizes      = product.productsizes.all()
            product_urls       = [image.url for image in product.productimages.all()]
            information_urls   = [information_image.url for information_image in product.informationimages.all()]
            size_price         = [{
                'size'  : product_size.size.size,
                'price' : product_size.price
                } for product_size in product.productsizes.all()]
            
            base_price = 0

            for i in size_price:
                if i['size'] == 'mini':
                    base_price = i['price']

            result = {
                'description'        : product.description,
                'name'               : product.name,
                'base_price'         : base_price,
                'size_price'         : size_price,
                'discount_rate'      : product.discount_rate,
                'product_images'     : product_urls,
                'information_images' : information_urls
            }
            
            return JsonResponse({"message" : result}, status = 200)

        except Product.DoesNotExist:
            return JsonResponse({"message" : "INVALID_PRODUCT"}, status = 404)