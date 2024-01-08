from django.urls import path
from .views import *

urlpatterns = [
    path('dishes/', food_dishes, name="food_dishes"),
    path('<str:food_id>/', food_detail_view, name="food_details"),
    path('remove/cart/<str:food_id>/', remove_cart, name="remove_cart")
]