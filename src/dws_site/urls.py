"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from dws_site.views import show_product_category, home_page, detail_product, \
    payment, about_us, delivery, blog

urlpatterns = [
    path("", home_page, name="home_page"),
    path('<slug:category_slug>/', show_product_category, name='show_product_category'),
    path('<slug:category_slug>/<slug:product_slug>/<int:product_id>',
         detail_product, name='detail_product'),
    path("payment", payment, name="payment"),
    path("about_us", about_us, name="about_us"),
    path("delivery", delivery, name="delivery"),
    path("blog", blog, name="blog"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
