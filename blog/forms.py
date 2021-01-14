from django import forms
from blog.models import BlogPost, Comment


class CreateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'category', 'time', 'calories',
                'ingredient_0',
                'ingredient_1',
                'ingredient_2',
                'ingredient_3',
                'ingredient_4',
                'ingredient_5',
                'ingredient_6',
                'ingredient_7',
                'ingredient_8',
                'ingredient_9',
                'ingredient_10',
                'ingredient_11',
                'ingredient_12',
                'ingredient_13',
                'ingredient_14',
                'ingredient_15',
                'ingredient_16',
                'ingredient_17',
                'ingredient_18',
                'ingredient_19',

                'step_0',
                'step_1',
                'step_2',
                'step_3',
                'step_4',
                'step_5',
                'step_6',
                'step_7',
                'step_8',
                'step_9',
                'step_10',
                'step_11',
                'step_12',
                'step_13',
                'step_14',
                'step_15',
                'step_16',
                'step_17',
                'step_18',
                'step_19',
        ]


class UpdateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'category', 'time', 'calories',
                'ingredient_0',
                'ingredient_1',
                'ingredient_2',
                'ingredient_3',
                'ingredient_4',
                'ingredient_5',
                'ingredient_6',
                'ingredient_7',
                'ingredient_8',
                'ingredient_9',
                'ingredient_10',
                'ingredient_11',
                'ingredient_12',
                'ingredient_13',
                'ingredient_14',
                'ingredient_15',
                'ingredient_16',
                'ingredient_17',
                'ingredient_18',
                'ingredient_19',

                'step_0',
                'step_1',
                'step_2',
                'step_3',
                'step_4',
                'step_5',
                'step_6',
                'step_7',
                'step_8',
                'step_9',
                'step_10',
                'step_11',
                'step_12',
                'step_13',
                'step_14',
                'step_15',
                'step_16',
                'step_17',
                'step_18',
                'step_19',]
    
    def save(self, commit=True):
        blog_post = self.instance
        blog_post.title = self.cleaned_data['title']
        blog_post.body = self.cleaned_data['body']
        blog_post.category = self.cleaned_data['category']
        blog_post.time = self.cleaned_data['time']
        blog_post.calories = self.cleaned_data['calories']

        blog_post.ingredient_0 = self.cleaned_data['ingredient_0']
        blog_post.ingredient_1 = self.cleaned_data['ingredient_1']
        blog_post.ingredient_2 = self.cleaned_data['ingredient_2']
        blog_post.ingredient_3 = self.cleaned_data['ingredient_3']
        blog_post.ingredient_4 = self.cleaned_data['ingredient_4']
        blog_post.ingredient_5 = self.cleaned_data['ingredient_5']
        blog_post.ingredient_6 = self.cleaned_data['ingredient_6']
        blog_post.ingredient_7 = self.cleaned_data['ingredient_7']
        blog_post.ingredient_8 = self.cleaned_data['ingredient_8']
        blog_post.ingredient_9 = self.cleaned_data['ingredient_9']
        blog_post.ingredient_10 = self.cleaned_data['ingredient_10']
        blog_post.ingredient_11 = self.cleaned_data['ingredient_11']
        blog_post.ingredient_12 = self.cleaned_data['ingredient_12']
        blog_post.ingredient_13 = self.cleaned_data['ingredient_13']
        blog_post.ingredient_14 = self.cleaned_data['ingredient_14']
        blog_post.ingredient_15 = self.cleaned_data['ingredient_15']
        blog_post.ingredient_16 = self.cleaned_data['ingredient_16']
        blog_post.ingredient_17 = self.cleaned_data['ingredient_17']
        blog_post.ingredient_18 = self.cleaned_data['ingredient_18']
        blog_post.ingredient_19 = self.cleaned_data['ingredient_19']

        blog_post.step_0 = self.cleaned_data['step_0']
        blog_post.step_1 = self.cleaned_data['step_1']
        blog_post.step_2 = self.cleaned_data['step_2']
        blog_post.step_3 = self.cleaned_data['step_3']
        blog_post.step_4 = self.cleaned_data['step_4']
        blog_post.step_5 = self.cleaned_data['step_5']
        blog_post.step_6 = self.cleaned_data['step_6']
        blog_post.step_7 = self.cleaned_data['step_7']
        blog_post.step_8 = self.cleaned_data['step_8']
        blog_post.step_9 = self.cleaned_data['step_9']
        blog_post.step_10 = self.cleaned_data['step_11']
        blog_post.step_11 = self.cleaned_data['step_11']
        blog_post.step_12 = self.cleaned_data['step_12']
        blog_post.step_13 = self.cleaned_data['step_13']
        blog_post.step_14 = self.cleaned_data['step_14']
        blog_post.step_15 = self.cleaned_data['step_15']
        blog_post.step_16 = self.cleaned_data['step_16']
        blog_post.step_17 = self.cleaned_data['step_17']
        blog_post.step_18 = self.cleaned_data['step_18']
        blog_post.step_19 = self.cleaned_data['step_19']
        



        if self.cleaned_data['image']:
            blog_post.image = self.cleaned_data['image']

        if commit:
            blog_post.save()
        return blog_post


class CreateCommentPostForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']