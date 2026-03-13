from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from items.views import home
from accounts.views import register
from users.views import account_dashboard, address_page


urlpatterns = [

    # admin
    path("admin/", admin.site.urls),

    # home
    path("", home, name="home"),

    # marketplace
    path("items/", include("items.urls")),

    # cart
    path("cart/", include(("cart.urls", "cart"), namespace="cart")),

    # account dashboard
    path("account/", account_dashboard, name="account"),

    # address page
    path("account/address/", address_page, name="address"),

    # register
    path("accounts/register/", register, name="register"),

    # login
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html"
        ),
        name="login"
    ),

    # logout
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)