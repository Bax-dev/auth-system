# Import necessary modules
from django.contrib import admin # Django admin module
from django.urls import path	 # URL routing
from account.views import * # Import views from the account app
from django.conf import settings # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # Static files serving

# Define URL patterns
urlpatterns = [
	path('', home, name="home"),	 # Home page
	path ('read/', index, name="index"),
	path('login/', login_page, name='login_page'), # Login page
	path('register/', register_page, name='register'), # Registration page
]

