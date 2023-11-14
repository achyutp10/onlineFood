from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('registerUser/', views.registerUser, name="registerUser"),
    path('registerVendor/', views.registerVendor, name="registerVendor"),
    
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),

]
