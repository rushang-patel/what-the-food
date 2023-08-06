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
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe-detail'),
    path('recipes/<int:recipe_id>/update/', views.recipes_update, name='recipe-update'),
    path('recipes/<int:recipe_id>/delete/', views.recipes_delete, name='recipe-delete'),
    path('recipes/search/', views.recipes_search, name='recipes-search'),
    path('recipes/tag/<str:tag>/', views.recipes_tag, name='recipes-tag'),
    path('recipes/category/<str:category>/', views.recipes_category, name='recipes-category'),
    
    path('meettheteam/', views.meet_the_team, name='meettheteam'),
    
    path('cuttingboard/form/', views.cuttingboard_form, name='cb-form'),
    path('cuttingboard/', views.cuttingboard_index, name='cb-index'),
    path('recipes/<int:recipe_id>/add-to-cutting-board/', views.add_to_cutting_board, name='add-to-cutting-board'),
    path('cuttingboard/<int:cutting_board_id>/', views.cuttingboard_detail, name='cb-detail'),
]