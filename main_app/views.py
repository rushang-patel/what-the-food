# main_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import logout
from .models import Recipe
from .forms import RecipeForm

def home(request):
    return render(request, 'home.html')

def redirect_to_home(request):
    return redirect('/')

def redirect_to_google_login(request):
    client_id = settings.GOOGLE_CLIENT_ID
    client_secret = settings.GOOGLE_CLIENT_SECRET

    redirect_uri = 'http://localhost:8000/accounts/google/login/callback/'
    scope = 'profile email'

    google_login_url = f"https://accounts.google.com/o/oauth2/auth?" \
                       f"client_id={client_id}" \
                       f"&redirect_uri={redirect_uri}" \
                       f"&response_type=code" \
                       f"&scope={scope}"

    return redirect(google_login_url)

def logout_and_redirect_to_home(request):
    logout(request)
    return redirect('/')

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            # Redirect to the detail page of the newly created recipe
            return redirect('recipe-detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()

    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipes_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

def recipe_update(request, recipe_id):
    # Retrieve the existing recipe object from the database
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        # Populate the form with the submitted data and files
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            # Save the updated recipe to the database
            form.save()
            recipe.save()
            # Redirect to the detail page of the updated recipe
            return redirect('recipe-detail', recipe_id=recipe.id)
    else:
        # Populate the form with the data from the existing recipe
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipe_delete(request, recipe_id):
    if request.method == 'POST':
        # Get the recipe object
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # Perform the deletion
        recipe.delete()
        # Redirect to the index.html page (recipes-index URL)
        return redirect('recipes-index')
    # For any other HTTP method (e.g., GET), show the detail.html page
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

def meet_the_team(request):
    return render(request, 'meettheteam.html')

