from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(0),
    ], null=True)
    comment = models.TextField(max_length=500, null=True)

    def __str__(self):
        return '%s - %s' % (self.user, self.rating)
