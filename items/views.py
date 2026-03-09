from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Item, Category
from .forms import ItemForm
from comments.forms import CommentForm


def item_list(request):
    items = Item.objects.select_related("category", "owner").all().order_by("-created_at")
    categories = Category.objects.all().order_by("name")

    selected_category = request.GET.get("category")
    if selected_category:
        items = items.filter(category__name=selected_category)

    return render(request, "items/item_list.html", {
        "items": items,
        "categories": categories,
        "selected_category": selected_category,
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

    return render(request, "items/item_form.html", {"form": form})


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(f"/admin/login/?next=/items/{item_id}/")

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = item
            comment.author = request.user
            comment.save()
            return redirect("item_detail", item_id=item.id)
    else:
        form = CommentForm()

    comments = item.comments.all()

    return render(request, "items/item_detail.html", {
        "item": item,
        "comments": comments,
        "form": form,
    })