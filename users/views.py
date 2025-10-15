from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import UserLoginForm



"""
class-based views:

view            = Generic View
ListView        = to display a list of records
DetailView      = to display a detail single record
CreateView      = to create a new record
UpdateView      = to update an existing record
DeleteView      = to delete an existing record
LoginView       = to handle user login

"""

# Create your views here.
class UserLogin(LoginView):
    template_name = "users/login.html"


class UserSignup(CreateView):
    model = User
    form_class = UserLoginForm
    template_name = "users/signup.html" 
    success_url = "user/login/"


