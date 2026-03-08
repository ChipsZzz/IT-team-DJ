from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from comments.forms import CommentForm

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