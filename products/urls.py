from django.urls import path
from products.views import ProductDetailView

urlpatterns = [
    path("/product/<id>", ProductDetailView.as_view()),
]