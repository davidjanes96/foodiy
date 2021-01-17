from django.urls import path
from feedback.views import (
    feedback_view,
    feedback_confirm_view,
)

app_name = 'feedback'

urlpatterns = [
        path('', feedback_view, name="feedback"),
        path('confirm/', feedback_confirm_view, name="feedback_confirm"),
    
] 