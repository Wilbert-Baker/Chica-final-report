from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

"""
Class-based views:

View         = Generic View
ListView     = get a list of records
DetailView   = get a single (detail) record
CreateView   = create a new record
DeleteView   = remove a record
UpdateView   = modify an existing record
LoginView    = LogIn

"""
# create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    
    
class PostDetail(DetailView):
    model = Post
    template_name = "blog/detail.html"
