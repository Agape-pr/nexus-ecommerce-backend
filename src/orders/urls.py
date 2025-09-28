from django.urls import path
from .views import CartDetailView, AddToCartView, RemoveFromCartView, CheckoutView, UserOrdersView

urlpatterns = [
    path("cart/", CartDetailView.as_view(), name="cart-detail"),
    path("cart/add/", AddToCartView.as_view(), name="cart-add"),
    path("cart/remove/", RemoveFromCartView.as_view(), name="cart-remove"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("orders/", UserOrdersView.as_view(), name="user-orders"),
]
