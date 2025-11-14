from django.views.generic import ListView, DetailView, CreateView, View, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render,redirect
from .models import Post, Comment
from .forms import CommentForm


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


def commentCreateView(request, pk):
    post = get_object_or_404(Post, pk=pk)


    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()

     
        return render (request, "blog/detail.html"), {'post':post, 'form':form}




def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)    
    post.delete()
    return redirect('post-list')  # Redirect to your list view or homepage

# send back to details page
#return redirect('post-detail', pk=post.id)
    
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

    
 




    

    
    
