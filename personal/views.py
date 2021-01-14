from django.shortcuts import render
from blog.models import BlogPost
from blog.views import get_blog_queryset
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

BLOG_POSTS_PER_PAGE = 10

# Create your views here.
def home_screen_view(request):
    
    context = {}

    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
    blog_posts_recent = sorted(BlogPost.objects.all(), key=attrgetter('date_published'), reverse=True)[:1]

    top_rated=0
    top_rated_blog=None
    for blog in BlogPost.objects.all():

        if blog.get_average() and blog.get_average() > top_rated:
            top_rated_blog = blog
            top_rated=blog.get_average()
    

    #stranice
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)

    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts'] = blog_posts
    context['blog_posts_recent'] = blog_posts_recent
    context['top_rated_blog'] = top_rated_blog

    return render(request, "personal/home.html", context)