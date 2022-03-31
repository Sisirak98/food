from .models import Carts,CartItem
from .views import cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Carts.objects.filter(c_id=cart_id(request))
            cart_items=CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except Carts.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)
