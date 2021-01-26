from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Avg, Count
from blog.models import BlogPost
from rating.models import Rating
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm, CreateCommentPostForm
from account.models import Account
from django.http import HttpResponse


def create_comment_view(request, slug):

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    
    form = CreateCommentPostForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(username=user.username).first()
        blog_post = get_object_or_404(BlogPost, slug=slug)
        obj.post = blog_post
        obj.author = author
        obj.save()

    return redirect(request.META['HTTP_REFERER']) 


def create_blog_view(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    
    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(username=user.username).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()

    context['form'] = form

    return render(request, "blog/create_blog.html", {})
    

def detail_blog_view(request, slug):

    context = {}

    blog_post = get_object_or_404(BlogPost, slug=slug)
    ratings = Rating.objects.filter(post=blog_post).order_by("score")

    is_favorite = False
    if blog_post.favorite.filter(id=request.user.id).exists():
        is_favorite = True

    average = ratings.aggregate(Avg("score"))["score__avg"]
    if average == None:
        average = 0
    average = round(average,1)

    count = ratings.aggregate(Count("score"))["score__count"]
    if count == None:
        count = 0

    context['blog_post'] = blog_post
    context['category'] = blog_post.get_category_display()
    context['average'] = average
    context['count'] = count
    context['is_favorite'] = is_favorite

    return render(request, 'blog/detail_blog.html', context)


def edit_blog_view(request, slug):

    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")

    blog_post = get_object_or_404(BlogPost, slug=slug)

    if blog_post.author != user:
        return HttpResponse("Niste autor ove objave.")

    if request.POST:
        form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Ažurirano."
            blog_post = obj
    form = UpdateBlogPostForm(
        initial = {
            "title": blog_post.title,
            "body": blog_post.body,
            "category": blog_post.category,
            "get_category_display": blog_post.get_category_display,
            "image": blog_post.image,
            "time": blog_post.time,
            "calories": blog_post.calories,
            "ingredient_0": blog_post.ingredient_0,
            "ingredient_1": blog_post.ingredient_1,
            "ingredient_2": blog_post.ingredient_2,
            "ingredient_3": blog_post.ingredient_3,
            "ingredient_4": blog_post.ingredient_4,
            "ingredient_5": blog_post.ingredient_5,
            "ingredient_6": blog_post.ingredient_6,
            "ingredient_7": blog_post.ingredient_7,
            "ingredient_8": blog_post.ingredient_8,
            "ingredient_9": blog_post.ingredient_9,
            "ingredient_10": blog_post.ingredient_10,
            "ingredient_11": blog_post.ingredient_11,
            "ingredient_12": blog_post.ingredient_12,
            "ingredient_13": blog_post.ingredient_13,
            "ingredient_14": blog_post.ingredient_14,
            "ingredient_15": blog_post.ingredient_15,
            "ingredient_16": blog_post.ingredient_16,
            "ingredient_17": blog_post.ingredient_17,
            "ingredient_18": blog_post.ingredient_18,
            "ingredient_19": blog_post.ingredient_19,
            "step_0": blog_post.step_0,
            "step_1": blog_post.step_1,
            "step_2": blog_post.step_2,
            "step_3": blog_post.step_3,
            "step_4": blog_post.step_4,
            "step_5": blog_post.step_5,
            "step_6": blog_post.step_6,
            "step_7": blog_post.step_7,
            "step_8": blog_post.step_8,
            "step_9": blog_post.step_9,
            "step_10": blog_post.step_10,
            "step_11": blog_post.step_11,
            "step_12": blog_post.step_12,
            "step_13": blog_post.step_13,
            "step_14": blog_post.step_14,
            "step_15": blog_post.step_15,
            "step_16": blog_post.step_16,
            "step_17": blog_post.step_17,
            "step_18": blog_post.step_18,
            "step_19": blog_post.step_19,

        }
    )
    context['form'] = form
    return render(request, 'blog/edit_blog.html', context)

def delete_blog_view(request, slug):
    context = {}
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post
    return render(request, 'blog/delete_blog.html', context)


def delete_blog_view_confirm(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    blog_post.delete()
    return render(request, 'blog/delete_blog_confirm.html')

def favorite_blog_view(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    
    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")

    if blog_post.favorite.filter(id=user.id).exists():
        blog_post.favorite.remove(user)
    else:
        blog_post.favorite.add(user)
    return HttpResponseRedirect(blog_post.get_absolute_url())

def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = BlogPost.objects.filter(
            Q(title__icontains=q) | 
            Q(body__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))
    

