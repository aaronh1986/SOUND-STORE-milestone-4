from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    blog_title = models.CharField(max_length=250, null=False, blank=False)
    blog_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="blog_post")
    blog_slug = models.SlugField(max_length=200)
    blog_heading = models.CharField(max_length=400, null=False, blank=False)
    blog_main = models.TextField()
    blog_image_url = models.URLField(max_length=1000, null=True, blank=True)
    blog_image = models.ImageField(null=True, blank=True)
