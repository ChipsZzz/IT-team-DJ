from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from items.models import Item
from .models import CartItem
from django.utils import timezone


@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum([c.item.price for c in cart_items])

    return render(request, "cart/cart.html", {
        "cart_items": cart_items,
        "total": total
    })


@login_required
def add_to_cart(request, id):
    item = get_object_or_404(Item, id=id)

    # ❗防止已售商品加入购物车
    if item.status == "sold":
        return redirect("item_detail", id=id)

    CartItem.objects.get_or_create(user=request.user, item=item)

    return redirect("cart:cart")


@login_required
def remove_from_cart(request, id):
    cart_item = get_object_or_404(CartItem, id=id, user=request.user)
    cart_item.delete()
    return redirect("cart:cart")


# =========================
# ⭐ 一键结算
# =========================

@login_required
def checkout_selected(request):

    if request.method == "POST":

        selected_ids = request.POST.getlist("selected_items")

        cart_items = CartItem.objects.filter(
            id__in=selected_ids,
            user=request.user
        )

        for cart in cart_items:
            item = cart.item

            if item.status == "available":
                item.status = "sold"
                item.buyer = request.user
                item.purchase_time = timezone.now()
                item.save()

            cart.delete()

    return redirect("purchase_history")