from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from blog.models import BlogPost

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect("home")


def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")
    
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "username": request.POST['username'],
                "email": request.POST['email'],
                "gender": request.POST['gender'],
                "get_gender_display": request.user.get_gender_display(),
                "date_of_birth": request.user.date_of_birth,
            }
            form.save()
            context['success_message'] = "Ažurirano"
        else:
            form.initial = {
                "username": request.POST['username'],
                "email": request.POST['email'],
                "gender": request.POST['gender'],
                "get_gender_display": request.user.get_gender_display(),
                "date_of_birth": request.user.date_of_birth,
            }


    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
                "gender": request.user.gender,
                "get_gender_display": request.user.get_gender_display(),
                "date_of_birth": request.user.date_of_birth,
            }
        )
    context['account_form'] = form
    


    blog_posts = BlogPost.objects.filter(author=request.user)
    favorite_posts = request.user.favorite.all()
    
    context['blog_posts'] = blog_posts
    context['favorite_posts'] = favorite_posts

    return render(request, 'account/account.html', context)


def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.html', {})

def favorite_blog_view_remove(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    
    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")

    if blog_post.favorite.filter(id=user.id).exists():
        blog_post.favorite.remove(user)
    else:
        blog_post.favorite.add(user)
    
    return redirect(request.META['HTTP_REFERER'])

     




