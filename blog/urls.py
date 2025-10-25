from django.urls import path
from .views import BlogListView, PostDetail, CommentCreateView, PostCreateView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("", BlogListView.as_view(), name='post-list'),
    path("detail/<int:pk>/", PostDetail.as_view(), name='post-detail'),
    path ("create_comment/",CommentCreateView.as_view(), name="create_comment"),
    path('post/new/', PostCreateView.as_view(), name="create_post"), 
]

