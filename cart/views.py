from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from items.models import Item
from .models import CartItem


@login_required
def cart_view(request):

    cart_items = CartItem.objects.filter(user=request.user)

    total = sum(item.item.price for item in cart_items)

    cart_count = cart_items.count()

    return render(request, "cart/cart.html", {
        "cart_items": cart_items,
        "total": total,
        "cart_count": cart_count
    })


@login_required
def add_to_cart(request, id):

    item = get_object_or_404(Item, id=id)

    CartItem.objects.create(
        user=request.user,
        item=item
    )

    return redirect("cart:cart")


@login_required
def remove_from_cart(request, id):

    cart_item = get_object_or_404(CartItem, id=id)

    if cart_item.user == request.user:
        cart_item.delete()

    return redirect("cart:cart")