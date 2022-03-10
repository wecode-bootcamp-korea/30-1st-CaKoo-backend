from django.urls import path, include

urlpatterns = [
    path("users", include('users.urls')),
    path("carts", include('carts.urls')),
    path("products", include('products.urls')),
    path("orders", include('orders.urls'))
]
