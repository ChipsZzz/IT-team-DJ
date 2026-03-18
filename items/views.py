from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Count

from .models import Item
from comments.models import Comment
from .forms import ItemForm


def home(request):

    latest_items = Item.objects.order_by("-created_at")[:6]

    popular_items = Item.objects.annotate(
        fav_count=Count("favourites")
    ).order_by("-fav_count")[:6]

    return render(request, "home.html", {
        "latest_items": latest_items,
        "popular_items": popular_items
    })


def item_list(request):

    query = request.GET.get("q", "")
    category = request.GET.get("category", "")

    items = Item.objects.all().order_by("-created_at")

    if query:
        items = items.filter(title__icontains=query)

    if category:
        items = items.filter(category=category)

    return render(request, "items/item_list.html", {
        "items": items,
        "query": query,
        "category": category
    })


def item_detail(request, id):

    item = get_object_or_404(Item, id=id)

    if request.method == "POST" and request.user.is_authenticated:

        text = request.POST.get("text")

        if text:
            Comment.objects.create(
                item=item,
                author=request.user,
                text=text
            )

        return redirect("item_detail", id=item.id)

    comments = item.comments.all().order_by("-created_at")

    return render(request, "items/item_detail.html", {
        "item": item,
        "comments": comments
    })


@login_required
def item_create(request):

    if request.method == "POST":

        form = ItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()

            return redirect("item_list")

    else:
        form = ItemForm()

    return render(request, "items/item_form.html", {
        "form": form
    })


@login_required
def my_items(request):

    items = Item.objects.filter(owner=request.user)

    return render(request, "items/my_items.html", {
        "items": items
    })


def seller_items(request, username):

    seller = get_object_or_404(User, username=username)

    items = Item.objects.filter(owner=seller)

    return render(request, "items/seller_items.html", {
        "seller": seller,
        "items": items
    })


@login_required
def toggle_favourite(request, id):

    item = get_object_or_404(Item, id=id)

    if request.method == "POST":
        if request.user in item.favourites.all():
            item.favourites.remove(request.user)
            favourited = False
        else:
            item.favourites.add(request.user)
            favourited = True

        return JsonResponse({
            "favourited": favourited,
            "count": item.favourites.count()
        })

    return JsonResponse({"error": "Invalid request"}, status=400)


@login_required
def favourite_items(request):

    items = request.user.favourite_items.all()

    return render(request, "items/favourites.html", {
        "items": items
    })

@login_required
def item_edit(request, id):

    item = get_object_or_404(Item, id=id)

    if item.owner != request.user:
        return redirect("item_detail", id=id)

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item_detail", id=id)

    else:
        form = ItemForm(instance=item)

    return render(request, "items/item_form.html", {
        "form": form
    })


@login_required
def item_delete(request, id):

    item = get_object_or_404(Item, id=id)

    if item.owner != request.user:
        return redirect("item_detail", id=id)

    if request.method == "POST":
        item.delete()
        return redirect("item_list")

    return render(request, "items/item_delete.html", {
        "item": item
    })


@login_required
def buy_item(request, id):

    item = get_object_or_404(Item, id=id)

    if item.status == "sold":
        return redirect("item_detail", id=id)

    item.status = "sold"
    item.buyer = request.user
    item.purchase_time = timezone.now()    
    item.save()

    return redirect("item_detail", id=id)


@login_required
def purchase_history(request):

    purchases = Item.objects.filter(buyer=request.user)

    sales = Item.objects.filter(owner=request.user, status="sold")

    return render(request, "items/purchase_history.html", {
        "purchases": purchases,
        "sales": sales
    })


from django.utils import timezone

@login_required
def checkout_selected(request):
    if request.method == "POST":
        item_ids = request.POST.getlist("selected_items")

        items = Item.objects.filter(id__in=item_ids, status="available")

        for item in items:
            item.status = "sold"
            item.buyer = request.user
            item.purchase_time = timezone.now()
            item.save()

        return redirect("cart:cart")


@login_required
def return_item(request, id):
    item = get_object_or_404(Item, id=id, buyer=request.user)

    item.status = "available"
    item.buyer = None
    item.is_returned = True
    item.return_time = timezone.now()
    item.save()

    return redirect("my_purchases")


@login_required
def my_purchases(request):
    items = Item.objects.filter(buyer=request.user)
    return render(request, "items/my_purchases.html", {"items": items})


@login_required
def my_sales(request):
    items = Item.objects.filter(owner=request.user, status="sold")
    return render(request, "items/my_sales.html", {"items": items})


from django.utils import timezone

@login_required
def return_item(request, id):

    item = get_object_or_404(Item, id=id, buyer=request.user)

    if item.status == "sold" and not item.is_returned:
        item.status = "available"
        item.buyer = None
        item.return_time = timezone.now()
        item.is_returned = True
        item.save()

    return redirect("purchase_history")