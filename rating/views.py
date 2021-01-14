from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from blog.models import BlogPost
from rating.models import Rating
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm
from rating.forms import RateBlogPostForm
from account.models import Account
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.generic import DeleteView
from django.urls import reverse_lazy, reverse


def rate_blog_view(request, slug):

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    blog_post = get_object_or_404(BlogPost, slug=slug)
     
    if Rating.objects.filter(user=request.user, post=blog_post):
        return HttpResponseRedirect(reverse('blog:detail', args=[str(slug)]))

    form = RateBlogPostForm(request.POST or None)
    obj = form.save(commit=False)
    user = Account.objects.filter(username=user.username).first()
    blog_post = get_object_or_404(BlogPost, slug=slug)
    post = blog_post
    score = request.POST.get('score')
    obj.user = user
    obj.post = post
    obj.score = score
    obj.save()

    return HttpResponseRedirect(reverse('blog:detail', args=[str(slug)]))
