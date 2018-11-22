from django.urls import path, include
from .views import checkout_show,submit_payment


urlpatterns = [
    path('', checkout_show, name='show_checkout'),
    path('submit_payment/',submit_payment, name='submit_payment'),
    ]