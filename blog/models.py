from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    owner = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=500, editable=False)

class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    body = models.TextField()
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=500, editable=False)
