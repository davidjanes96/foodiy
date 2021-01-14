from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.db.models import Avg
from rating.models import Rating

def upload_location(instance, filename, **kwargs):
    file_path = 'blog/{author_id}/{title}={filename}'.format(
        author_id=str(instance.author.id), 
        title=str(instance.title), 
        filename=filename,
    )
    return file_path

CATEGORY_CHOICES = (
    (0, 'Kategorija'),
    (1, 'Doručak'),
    (2, 'Hladno predjelo'),
    (3, 'Toplo predjelo'),
    (4, 'Glavno jelo'),
    (5, 'Desert'),
    (6, 'Salate'),
    (7, 'Prilozi'),
    (8, 'Ostalo'),
)

class BlogPost(models.Model):
    title           = models.CharField(max_length=50, null=False, blank=False)
    body            = models.TextField(max_length=500, null=False, blank=False)
    image           = models.ImageField(upload_to=upload_location, null=False, blank=False)
    date_published  = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated    = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category        = models.IntegerField(verbose_name="Kategorija", choices=CATEGORY_CHOICES, default=0)
    slug            = models.SlugField(blank=True, unique=True)
    time            = models.IntegerField(null=True, blank=True)
    calories        = models.IntegerField(null=True, blank=True)    

    ingredient_0    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_1    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_2    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_3    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_4    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_5    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_6    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_7    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_8    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_9    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_10    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_11    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_12    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_13    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_14    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_15    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_16    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_17    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_18    = models.CharField(max_length=50, null=True, blank=True)
    ingredient_19    = models.CharField(max_length=50, null=True, blank=True)

    step_0    = models.CharField(max_length=500, null=True, blank=True)
    step_1    = models.CharField(max_length=500, null=True, blank=True)
    step_2    = models.CharField(max_length=500, null=True, blank=True)
    step_3    = models.CharField(max_length=500, null=True, blank=True)
    step_4    = models.CharField(max_length=500, null=True, blank=True)
    step_5    = models.CharField(max_length=500, null=True, blank=True)
    step_6    = models.CharField(max_length=500, null=True, blank=True)
    step_7    = models.CharField(max_length=500, null=True, blank=True)
    step_8    = models.CharField(max_length=500, null=True, blank=True)
    step_9    = models.CharField(max_length=500, null=True, blank=True)
    step_10    = models.CharField(max_length=500, null=True, blank=True)
    step_11    = models.CharField(max_length=500, null=True, blank=True)
    step_12    = models.CharField(max_length=500, null=True, blank=True)
    step_13    = models.CharField(max_length=500, null=True, blank=True)
    step_14    = models.CharField(max_length=500, null=True, blank=True)
    step_15    = models.CharField(max_length=500, null=True, blank=True)
    step_16    = models.CharField(max_length=500, null=True, blank=True)
    step_17    = models.CharField(max_length=500, null=True, blank=True)
    step_18    = models.CharField(max_length=500, null=True, blank=True)
    step_19    = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_average(self):
        ratings = Rating.objects.filter(post=self)
        average = ratings.aggregate(Avg("score"))["score__avg"]
        return average




@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.title)
    
pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)

class Comment(models.Model):
    post            = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)
    author          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body            = models.TextField()
    date_added      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author)
