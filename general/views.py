from django.shortcuts import render
from foods.models import Food, Cart
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.shortcuts import get_object_or_404


def home(request):
    foods = Food.objects.all()[:8]
    context = {
        'foods': foods
    }
    return render(request, 'general/home.html', context)

@login_required
def cart(request):
    carts = Cart.objects.filter(user=request.user)
    total_prices = [cart_item.total_price() for cart_item in carts]
    total_cart_price = sum(total_prices)
    context = {
        'carts': carts,
        'total_cart_price': total_cart_price
    }
    return render(request, 'general/cart.html', context)

def about(request):
    return render(request, 'general/about.html')

def search(request):
    return render(request, 'general/search.html')