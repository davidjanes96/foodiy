from django.urls import path
from rating.views import (
    rate_blog_view,
)

app_name = 'rate'

urlpatterns = [
        path('<slug>/rate', rate_blog_view, name="rate_post"),
    
] 