from django.urls import path
from django.urls.conf import include

from web.views import index, product, subscribe, contact

app_name = "web"


urlpatterns = [
    path('',index,name="index"),
    path('subscribe',subscribe,name="subscribe"),
    path('contact',contact,name="contact"),
    path('product',product,name="product")

]