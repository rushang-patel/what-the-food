from django.contrib import admin
from django.urls import path, include
from main_app import views as main_app_views
from django.contrib.auth.decorators import login_required

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
    path('recipes/create/', login_required(main_app_views.recipe_create), name='recipe-create'),
    path('recipes/', main_app_views.recipes_index, name='recipes-index'),
    path('recipes/<int:recipe_id>/', main_app_views.recipe_detail, name='recipe-detail'),
    path('recipes/<int:recipe_id>/update/', main_app_views.recipes_update, name='recipe-update'),
    path('recipes/<int:recipe_id>/delete/', main_app_views.recipes_delete, name='recipe-delete'),
    
    path('meet-the-team/', main_app_views.meet_the_team, name='meet-the-team'),
    
    path('cuttingboard/form/', main_app_views.cuttingboard_form, name='cb-form'),
    path('cuttingboard/', main_app_views.cuttingboard_index, name='cb-index'),
    path('recipes/<int:recipe_id>/add-to-cutting-board/', main_app_views.add_to_cutting_board, name='add-to-cutting-board'),
    path('cuttingboard/<int:cutting_board_id>/', main_app_views.cuttingboard_detail, name='cb-detail'),
    ]
