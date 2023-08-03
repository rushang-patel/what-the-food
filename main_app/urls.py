from django.urls import path, include
from . import views

urlpatterns = [
    # Your custom login view
    path('accounts/login/', views.redirect_to_google_login, name='account_login'),

    # Other URL patterns for the main_app
    path('', views.home, name='home'),
    path('main_app/', include('main_app.urls')),
    path('accounts/profile/', views.redirect_to_home, name='profile'),
    path('logout/', views.logout_and_redirect_to_home, name='logout'),
    path('recipes/', views.recipes_index, name='index'),
    path('recipes/recipe_form/',views.recipe_form, name='recipe-form'),
    path('recipes/create/', views.recipe_create, name='recipe-create'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='detail'), 
    path('recipes/<int:recipe_id>/update/', views.recipes_update, name='update'),
    path('recipes/<int:recipe_id>/delete/', views.recipes_delete, name='delete'),
    path('recipes/search/', views.recipes_search, name='search'),
    path('recipes/tag/<str:tag>/', views.recipes_tag, name='tag'),
    path('recipes/category/<str:category>/', views.recipes_category, name='category'),
]

