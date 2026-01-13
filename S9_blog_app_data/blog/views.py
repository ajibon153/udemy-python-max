from django.shortcuts import render, get_object_or_404
from .models import Post
# from logging import getLogger
# Create your views here.


def home_page(request):
    # sorted_posts = all_posts.sort(key=get_date) # Sort the posts list by date and replace the old list
    # Sort the posts list by date to the new list
    latest_posts = Post.objects.all().order_by('-date')[:3]  # get first 3 data
    return render(request, 'blog/index.html', {'posts': latest_posts})


def posts(request):
    all_posts = Post.objects.all().order_by('-date')  # get first 3 data
    return render(request, 'blog/all-posts.html', {"all_posts": all_posts})


def post_detail(request, slug):
    # identifiedPost = next(post for post in all_posts if post["slug"] == slug)
    # identifiedPost = Post.objects.get(slug=slug)
    identifiedPost = get_object_or_404(Post, slug=slug)
    # print('========== identifiedPost', identifiedPost.__dict__)
    # print('Tags:', identifiedPost.tag)
    # for tag in identifiedPost.tag.all():
    #     print('Tag:', tag)

    return render(request, 'blog/post_detail.html', {'post': identifiedPost, 'tags': identifiedPost.tag.all()})
