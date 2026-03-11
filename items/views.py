from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

from .models import Item
from comments.models import Comment
from .forms import ItemForm


def home(request):
    latest_items = Item.objects.order_by("-created_at")[:6]

    return render(request, "home.html", {
        "latest_items": latest_items
    })


def item_list(request):

    query = request.GET.get("q", "")

    items = Item.objects.all().order_by("-created_at")

    if query:
        items = items.filter(title__icontains=query)

    return render(request, "items/item_list.html", {
        "items": items,
        "query": query
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


@login_required
def favourite_items(request):

    items = request.user.favourite_items.all()

    return render(request, "items/favourites.html", {
        "items": items
    })