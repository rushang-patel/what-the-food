"""
URL configuration for whatthefood project.

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
from django.contrib import admin
from django.urls import path, include
from main_app import views as main_app_views

urlpatterns = [
    # Django admin site
    path('admin/', admin.site.urls),

    # Django-allauth URLs for authentication
    path('accounts/', include('allauth.urls')),

    # Custom URL patterns for your main_app
    path('', main_app_views.home, name='home'),
    path('accounts/profile/', main_app_views.redirect_to_home, name='profile'),
    path('accounts/login/', main_app_views.redirect_to_google_login, name='account_login'),
    path('logout/', main_app_views.logout_and_redirect_to_home, name='logout'),
]
