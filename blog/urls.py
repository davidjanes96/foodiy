from django.urls import path
from blog.views import (
    create_blog_view,
    detail_blog_view,
    edit_blog_view,
    delete_blog_view,
    delete_blog_view_confirm,
    create_comment_view,
    favorite_blog_view,
)

app_name = 'blog'

urlpatterns = [
    path('create/', create_blog_view, name="create"),
    path('<slug>/', detail_blog_view, name="detail"),
    path('<slug>/edit', edit_blog_view, name="edit"),
    path('<slug>/delete', delete_blog_view, name="delete"),
    path('<slug>/favorite', favorite_blog_view, name="favorite"),
    path('<slug>/delete-confirm', delete_blog_view_confirm, name="delete-confirm"),
    path('<slug>/comment', create_comment_view, name="comment")
    
] 