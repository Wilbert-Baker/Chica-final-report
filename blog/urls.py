from django.urls import path
from .views import BlogListView, PostDetail, commentCreateView,delete_post, PostCreateView
from django.contrib.auth import views as auth_views
from django.views.generic import DeleteView
from .models import Post



urlpatterns = [
    path("", BlogListView.as_view(), name='post-list'),
    path("detail/<int:pk>/", PostDetail.as_view(), name='post-detail'),
    path("post/<int:pk>/create_comment/", commentCreateView, name="create_comment"),
    path('post/new/', PostCreateView.as_view(), name="create_post"), 
    path('post/delete/<int:pk>', delete_post, name="test_delete"), 
    path('post/<int:pk>/delete/', DeleteView.as_view(model=Post, success_url='/', template_name='blog/post_confirm_delete.html'))
]

