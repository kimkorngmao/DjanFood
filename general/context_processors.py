from foods.models import Cart

def cart_count(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user).count
        if carts:
            return {'cart_count': carts}  # Replace with your quantity calculation
        else:
            return {'cart_count': 0}
    else:
        return {'cart_count': 0}
