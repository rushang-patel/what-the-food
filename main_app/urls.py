from django.urls import path
from . import views

urlpatterns = [
    # Your custom login view
    path('accounts/login/', views.redirect_to_google_login, name='account_login'),

    # URL patterns for the main_app
    path('', views.home, name='home'),
    path('accounts/profile/', views.redirect_to_home, name='profile'),
    path('logout/', views.logout_and_redirect_to_home, name='logout'),
    path('recipes/', views.recipes_index, name='recipes-index'),
    path('recipes/recipe_form/', views.recipe_form, name='recipe-form'),
    path('recipes/create/', views.recipe_create, name='recipe-create'),
    path('recipes/<int:recipe_id>/detail/', views.recipe_detail, name='recipe-detail'),
    path('recipes/<int:recipe_id>/update/', views.recipe_update, name='recipe-update'),
    path('recipes/<int:recipe_id>/delete/', views.recipe_delete, name='recipe-delete'),
    path('meettheteam/', views.meet_the_team, name='meet-the-team'),
]

