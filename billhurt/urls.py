"""billhurt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Post

info_dict = {
    "queryset": Post.objects.all(),
    "date_field": "created_at",
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": {"post": GenericSitemap(info_dict)}},
    ),
]