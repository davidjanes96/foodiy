from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Rating(models.Model):
    user = models.ForeignKey("account.Account", on_delete=models.CASCADE, null=True)
    post = models.ForeignKey("blog.BlogPost", on_delete=models.CASCADE, null=True, related_name="post")
    score = models.PositiveSmallIntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(0),
    ], null=True)

    def __str__(self):
        return str('%s - %s - %s' % (self.user, self.post, self.score))
