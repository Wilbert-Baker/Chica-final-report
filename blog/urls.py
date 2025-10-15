from django.urls import path
from .views import BlogListView, PostDetail

urlpatterns = [
    path("", BlogListView.as_view(), name='post-list'),
    path("detail/<int:pk>/", PostDetail.as_view(), name='post-detail'),
]