from django.contrib import admin
from django.urls import path
from  .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-need/', views.add_need, name='add_need'),
    path('advertise-contract/', views.advertise_contract, name='advertise_contract'),
]