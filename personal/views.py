from django.shortcuts import render
from blog.models import BlogPost
from blog.views import get_blog_queryset
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

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

def categories_screen_view(request):
    
    context = {}

    blog_posts_recent = sorted(BlogPost.objects.all(), key=attrgetter('date_published'), reverse=True)[:1]

    top_rated=0
    top_rated_blog=None
    for blog in BlogPost.objects.all():

        if blog.get_average() and blog.get_average() > top_rated:
            top_rated_blog = blog
            top_rated=blog.get_average()

    context['blog_posts_recent'] = blog_posts_recent
    context['top_rated_blog'] = top_rated_blog

    return render(request, "personal/categories.html", context)

def category_view(request, cats, sort):
    
    context = {}

    blog_posts_recent = sorted(BlogPost.objects.all(), key=attrgetter('date_published'), reverse=True)[:1]

    top_rated=0
    top_rated_blog=None
    for blog in BlogPost.objects.all():

        if blog.get_average() and blog.get_average() > top_rated:
            top_rated_blog = blog
            top_rated=blog.get_average()

    if sort == 1:
        category_posts = sorted(BlogPost.objects.filter(category=cats), key=attrgetter('date_published'), reverse=True)
    elif sort == 2:
        category_posts = sorted(BlogPost.objects.filter(category=cats), key=attrgetter('date_updated'), reverse=True)
    elif sort == 3:
        category_posts = sorted(BlogPost.objects.filter(category=cats), key=attrgetter('calories'))
    elif sort == 4:
        category_posts = sorted(BlogPost.objects.filter(category=cats), key=attrgetter('calories'), reverse=True)
    elif sort == 5:
        category_posts = sorted(BlogPost.objects.filter(category=cats), key=attrgetter('time'))
    elif sort == 6:
        category_posts = sorted(BlogPost.objects.filter(category=cats), key=attrgetter('time'), reverse=True)
    else:
        category_posts = sorted(BlogPost.objects.filter(category=cats), key=attrgetter('date_published'), reverse=True)

    #stranice
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(category_posts, BLOG_POSTS_PER_PAGE)

    try:
        category_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        category_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        category_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)


    context['blog_posts_recent'] = blog_posts_recent
    context['top_rated_blog'] = top_rated_blog
    context['cats'] = cats
    context['sort'] = sort
    context['category_posts'] = category_posts

    return render(request, 'personal/category.html', context)
