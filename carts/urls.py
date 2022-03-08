from unittest.mock import patch
from django.urls import path
from carts.views import CartView

urlpatterns = [
    path("", CartView.as_view()),
    path("/delete-cart", CartView.delete),
]