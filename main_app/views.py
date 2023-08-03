from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import logout

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def redirect_to_home(request):
    return redirect('/')

def redirect_to_google_login(request):
    # Get the client ID and secret from settings.py
    client_id = settings.GOOGLE_CLIENT_ID
    client_secret = settings.GOOGLE_CLIENT_SECRET

    # Replace 'YOUR_REDIRECT_URI' and 'SCOPE' with your actual values
    redirect_uri = 'http://localhost:8000/accounts/google/login/callback/'
    scope = 'profile email'

    # Construct the Google OAuth login URL
    google_login_url = f"https://accounts.google.com/o/oauth2/auth?" \
                       f"client_id={client_id}" \
                       f"&redirect_uri={redirect_uri}" \
                       f"&response_type=code" \
                       f"&scope={scope}"

    # Redirect the user to the Google login page
    return redirect(google_login_url)

def logout_and_redirect_to_home(request):
    logout(request)
    return redirect('/')
  
def meet_the_team(request):
    return render(request, 'meettheteam.html')
