from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from .models import *
from django.urls import reverse
from django.db.models import Sum

# Create your views here.

def food_dishes(request):
    foods = Food.objects.all()
    context = {
        'foods': foods
    }
    return render(request, 'foods/food_dishes.html', context)

def food_detail_view(request, food_id):
    food = Food.objects.get(id=food_id)
    try:
        cart_item = Cart.objects.get(user=request.user, food=food)  # Get the relevant cart item
        food_in_cart_quantity = cart_item.quantity
    except:
        food_in_cart_quantity = 1
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
        cart_items_count = carts.count()
        cart_items_count = carts.aggregate(Sum('quantity'))['quantity__sum']
        total_prices = [cart_item.total_price() for cart_item in carts]
        total_cart_price = sum(total_prices)
    # Add or update food cart
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(reverse('login') + '?next=' + request.path)
        quantity = int(request.POST.get('food-quantity'))
        # Check for existing cart item and update quantity if found
        if quantity > 0:
            cart_item, created = Cart.objects.update_or_create(
                user=request.user, food=food,
                defaults={'quantity': quantity}
            )
        else:
            try:
                Cart.objects.get(user=request.user, food=food).delete()
            except:
                pass
        return redirect(reverse('food_details', args=[food_id]))
    context = {
        'food': food,
        'food_in_cart_quantity': food_in_cart_quantity
    }
    if request.user.is_authenticated:
        context['cart_items_count'] = cart_items_count
        context['total_cart_price'] = total_cart_price
    return render(request, 'foods/food_details.html', context)

def remove_cart(request, food_id):
    if request.method == "POST":
        food = Food.objects.get(id=food_id)
        Cart.objects.get(user=request.user, food=food).delete()
        return redirect('cart')
    else:
        return HttpResponseNotAllowed(['POST'])