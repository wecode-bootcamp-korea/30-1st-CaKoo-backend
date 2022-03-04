from genericpath import exists
import json

from django.http      import JsonResponse
from django.views     import View
from products.models  import Product
from users.utils      import login_decorator

class ProductDetailView(View):
    @login_decorator
    def post(self, request, id):
        try:
            data               = json.loads(request.body)
            product_id         = id
            product            = Product.objects.get(id = product_id)
            product_images     = product.productimages.filter(product = product)
            information_images = product.informationimages.filter(product = product)
            product_urls       = []
            information_urls   = []

            for information_image in information_images:
                information_urls.append(information_image.url)

            for image in product_images:
                product_urls.append(image.url)

            if data.get('size_id') == None:
                sizes      = product.sizes.all()
                size_list  = []

                for size in sizes:
                    size_list.append(size.size)

                result = {
                    'descriptin'         : product.description,
                    'name'               : product.name,
                    'price'              : product.productsizes.filter(product_id = product_id, size_id = 1)[0].price,
                    'size'               : size_list,
                    'discount_rate'      : product.discount_rate,
                    'product_images'     : product_urls,
                    'information_images' : information_urls
                }

                return JsonResponse({"message" : result})

            if  data.get('size_id'):
                size_id = data['size_id']
                result = {
                    'descriptin'         : product.description,
                    'name'               : product.name,
                    'price'              : product.productsizes.filter(product_id = product_id, size_id = size_id)[0].price,
                    'size'               : product.productsizes.filter(product_id = product_id, size_id = size_id)[0].size.size,
                    'discount_rate'      : product.discount_rate,
                    'product_images'     : product_urls,
                    'information_images' : information_urls
                }

                return JsonResponse({"message" : result}, status = 200)

        except Product.DoesNotExist:
            return JsonResponse({"message" : "INVALID_PRODUCT"})

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)