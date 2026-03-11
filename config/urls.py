from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from items.views import home
from accounts.views import register

urlpatterns = [

    path("admin/", admin.site.urls),

    # 首页
    path("", home, name="home"),

    # marketplace
    path("items/", include("items.urls")),

    # 注册
    path("accounts/register/", register, name="register"),

    # 登录
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html"
        ),
        name="login"
    ),

    # 登出
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)