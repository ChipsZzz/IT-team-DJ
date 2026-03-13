from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Address


@login_required
def account_dashboard(request):

    return render(request, "accounts/dashboard.html")


@login_required
def address_page(request):

    address, created = Address.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        address.city = request.POST.get("city")
        address.postcode = request.POST.get("postcode")
        address.address_line = request.POST.get("address")

        address.save()

    return render(request, "accounts/address.html", {
        "address": address
    })