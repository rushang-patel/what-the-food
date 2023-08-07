# main_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseForbidden
from .forms import RecipeForm, CuttingBoardForm
from .models import Recipe, CuttingBoard

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

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user  # Associate the recipe with the current user
            recipe.save()
            return redirect('recipe-detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(user=request.user)

    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipes_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    cutting_boards = CuttingBoard.objects.all()

    if request.method == 'POST':
        cutting_board_id = request.POST.get('cutting_board_id')
        if cutting_board_id:
            cutting_board = get_object_or_404(CuttingBoard, id=cutting_board_id)
            recipe.cutting_boards.add(cutting_board)

    return render(request, 'recipes/detail.html', {'recipe': recipe})

@login_required
def recipes_update(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    # Check if the current user is the owner of the recipe
    if request.user != recipe.user:
        return HttpResponseForbidden("You don't have permission to edit this recipe.")

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

@login_required
def recipes_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    # Check if the current user is the owner of the recipe
    if request.user != recipe.user:
        return HttpResponseForbidden("You don't have permission to delete this recipe.")

    if request.method == 'POST':
        # Perform the deletion
        recipe.delete()
        # Redirect to the index.html page (recipes-index URL)
        return redirect('recipes-index')

    # For any other HTTP method (e.g., GET), show the detail.html page
    return render(request, 'recipes/detail.html', {'recipe': recipe})

def meet_the_team(request):
    return render(request, 'meettheteam.html')



@login_required
def cuttingboard_form(request):
    if request.method == 'POST':
        form = CuttingBoardForm(request.POST)
        if form.is_valid():
            cutting_board = form.save(commit=False)
            cutting_board.user = request.user
            cutting_board.save()
            return redirect('cb-index')
    else:
        form = CuttingBoardForm()

    return render(request, 'cuttingboard/cuttingboard_form.html', {'form': form})

@login_required
def cuttingboard_index(request):
    cutting_boards = CuttingBoard.objects.filter(user=request.user)
    return render(request, 'cuttingboard/cbindex.html', {'cutting_boards': cutting_boards})

def cuttingboard_detail(request, cutting_board_id):
    cuttingboard = get_object_or_404(CuttingBoard, id=cutting_board_id, user=request.user)
    return render(request, 'cuttingboard/cbdetail.html', {'cuttingboard': cuttingboard})

def add_to_cutting_board(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)
    if request.method == 'POST':
        cutting_board_id = request.POST.get('cutting_board_id')
        if cutting_board_id:
            cutting_board = get_object_or_404(CuttingBoard, id=cutting_board_id)
            recipe.cutting_boards.add(cutting_board)
            return redirect('recipe-detail', recipe_id=recipe.id)
    return redirect('recipe-detail', recipe_id=recipe.id)