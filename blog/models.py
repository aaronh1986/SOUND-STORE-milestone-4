from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               null=False, blank=False)
    blog_title = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField(max_length=200)
    post_head = models.CharField(max_length=400, null=False, blank=False)
    post_main = models.TextField()
    email = models.EmailField(max_length=254, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.blog_title
