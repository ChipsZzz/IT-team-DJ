from django.urls import path
from . import views

urlpatterns = [

    path("", views.item_list, name="item_list"),

    path("create/", views.item_create, name="item_create"),

    path("my/", views.my_items, name="my_items"),

    path("favourites/", views.favourite_items, name="favourite_items"),

    path("seller/<str:username>/", views.seller_items, name="seller_items"),

    path("history/", views.purchase_history, name="purchase_history"),

    path("<int:id>/", views.item_detail, name="item_detail"),

    path("<int:id>/edit/", views.item_edit, name="item_edit"),

    path("<int:id>/delete/", views.item_delete, name="item_delete"),

    path("<int:id>/buy/", views.buy_item, name="buy_item"),

    path("<int:id>/favourite/", views.toggle_favourite, name="toggle_favourite"),

]