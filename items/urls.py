from django.urls import path
from . import views

urlpatterns = [

    path("", views.item_list, name="item_list"),

    path("create/", views.item_create, name="item_create"),

    path("my/", views.my_items, name="my_items"),

    path("favourites/", views.favourite_items, name="favourite_items"),

    path("seller/<str:username>/", views.seller_items, name="seller_items"),

    path("<int:id>/", views.item_detail, name="item_detail"),

    path("<int:id>/favourite/", views.toggle_favourite, name="toggle_favourite"),

]