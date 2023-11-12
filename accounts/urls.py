from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('registerUser/', views.registerUser, name="registerUser"),
    path('registerVendor/', views.registerVendor, name="registerVendor"),
]
