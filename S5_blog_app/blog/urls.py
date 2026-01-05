from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.post_detail,
         name='detail-posts-page'),  # /posts/my-first-post
]
