from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique_for_date='published_date')
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField(default='blog post')
    status = models.CharField(max_length=10, choices=options, default='draft')
    image = models.ImageField(default = '/static/img/TikTok Ads.jpg', upload_to='static/img')
    caption = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_single", args=[self.slug])

    class Meta:
        ordering = ('-published_date', )
    

    