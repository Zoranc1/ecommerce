"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from accounts.views import signup, show_profile
from products.views import products_list, products_detail
from checkout import urls as checkout_urls
from cart import urls as cart_urls
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products_list, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
    path('cart/', include(cart_urls)),
   
    path('checkout/', include(checkout_urls)),
    
    path('product_details/<int:id>', products_detail, name='products_detail'),
    path('accounts/profile', show_profile, name='profile'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
    
