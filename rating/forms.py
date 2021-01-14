from django import forms
from rating.models import Rating

class RateBlogPostForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['user', 'post', 'score']

    def save(self, commit=True):
        rate_post = self.instance
        #rate_post.user = self.cleaned_data['user']
        #rate_post.post = self.cleaned_data['post']
        #rate_post.score = self.cleaned_data['score']

        if commit:
            rate_post.save()
        return rate_post