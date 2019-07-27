from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    name = models.CharField(max_length=100, verbose_name="Name")
    body = models.TextField(max_length=2000, verbose_name="Description")
    published = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(to=User, verbose_name='Publisher', related_name='post_user', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

