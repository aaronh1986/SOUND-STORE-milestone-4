from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'blog_title',
        'author',
        'post_head',
        'post_main',
        'email',
        'image_url',
        'image',
        'created_on',
    )

    ordering = ('-created_on')


admin.site.register(BlogPost, BlogPostAdmin)
