from django import forms
from feedback.models import Feedback

class CreateFeedback(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['rating', 'comment']