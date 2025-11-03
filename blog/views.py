from django.views.generic import ListView, DetailView, CreateView, View 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from .models import Post, Comment


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
class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/post_list.html"
    
    
class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/detail.html"

class CommentCreateView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'next'


    def post(self, request):
        id = request.POST.get("id") 
        comment = request.POST.get("comment")

        #get the post object
        post = Post.objects.get(pk=id)
    
        #create comment 
        Comment.objects.create(
            post=post,
            author=request.user,
            body=comment
        )

        # send back to details page
        return redirect('post-detail', pk=post.id)
    
class PostCreateView(LoginRequiredMixin, CreateView):
        login_url = '/login/'
        redirect_field_name = 'next'


        model = Post
        fields = '__all__'
        template_name = 'blog/post_form.html' # corrected path
        success_url = '/blog/' # optional redirect after creation


        def form_valid(self, form):
             # Automatically sey the post author to the login.user
             form. instance.author = self.request.user
             return super().form_valid(form) 

    
 




    

    
    
