from django.urls import path
from . import views

urlpatterns = [
    # Your custom login view
    path('accounts/login/', views.redirect_to_google_login, name='account_login'),

    # Other URL patterns for the main_app
    path('', views.home, name='home'),
    path('accounts/profile/', views.redirect_to_home, name='profile'),
    path('logout/', views.logout_and_redirect_to_home, name='logout'),
]

