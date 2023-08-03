from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import logout
from .forms import RecipeForm
from .models import Recipe

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
            title = form.cleaned_data['title']
            prep_time = form.cleaned_data['prep_time']
            ingredients = form.cleaned_data['ingredients']
            steps = form.cleaned_data['steps']
            optional_link = form.cleaned_data['optional_link']
            upload_file = request.FILES['upload_file']
            checkboxes = form.cleaned_data['checkboxes']

            recipe = Recipe(
                title=title,
                prep_time=prep_time,
                ingredients=ingredients,
                steps=steps,
                optional_link=optional_link,
                upload_file=upload_file,
                checkboxes=','.join(checkboxes),
            )
            recipe.save()

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

def recipes_update(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    # Add your update logic here
    # ...
    return render(request, 'recipes/update.html', {'recipe': recipe})

def recipes_delete(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    # Add your delete logic here
    # ...
    return redirect('recipes-index')

def recipes_search(request):
    # Add your search logic here
    # ...
    return render(request, 'recipes/search.html')

def recipes_tag(request, tag):
    # Add your tag logic here
    # ...
    return render(request, 'recipes/tag.html')

def recipes_category(request, category):
    # Add your category logic here
    # ...
    return render(request, 'recipes/category.html')

def recipe_form(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            prep_time = form.cleaned_data['prep_time']
            ingredients = form.cleaned_data['ingredients']
            steps = form.cleaned_data['steps']
            optional_link = form.cleaned_data['optional_link']
            upload_file = request.FILES['upload_file']
            checkboxes = form.cleaned_data['checkboxes']

            recipe = Recipe(
                title=title,
                prep_time=prep_time,
                ingredients=ingredients,
                steps=steps,
                optional_link=optional_link,
                upload_file=upload_file,
                checkboxes=','.join(checkboxes),
            )
            recipe.save()

            return redirect('recipe-detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()

    return render(request, 'recipes/recipe_form.html', {'form': form})
  
def meet_the_team(request):
    return render(request, 'meettheteam.html')
