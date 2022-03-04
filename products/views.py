import json

from django.http      import JsonResponse
from django.views     import View

from products.models  import Product

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product            = Product.objects.get(id = product_id)
            product_images     = product.productimages.all()
            information_images = product.informationimages.all()
            product_sizes      = product.productsizes.all()
            product_urls       = [image.url for image in product_images]
            information_urls   = [information_image.url for information_image in information_images]
            size_price         = [{'size' : product_size.size.size , 'price' : product_size.price} for product_size in product_sizes]

            result = {
                'description'        : product.description,
                'name'               : product.name,
                'base_price'         : product_sizes[0].price,
                'size_price'         : size_price,
                'discount_rate'      : product.discount_rate,
                'product_images'     : product_urls,
                'information_images' : information_urls
            }
            
            return JsonResponse({"message" : result}, status = 200)

        except Product.DoesNotExist:
            return JsonResponse({"message" : "INVALID_PRODUCT"}, status = 404)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)