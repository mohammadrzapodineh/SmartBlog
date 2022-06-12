from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .managers import BlogManager
from django.urls import reverse_lazy
from taggit.managers import TaggableManager


class Post(models.Model):
    status_choices = (
        ('draft', 'draft'),
        ('publish', 'publish')

    )
    title = models.CharField(verbose_name='title', max_length=240)
    body = models.TextField(verbose_name='Text')
    author = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    status = models.CharField(choices=status_choices, max_length=10, verbose_name='status', default='publish')
    # Managers
    objects = models.Manager()
    published = BlogManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return f'Post:{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('Blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='post')
    name = models.CharField(max_length=200, verbose_name='user name')
    email = models.EmailField(verbose_name='user email')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    text = models.TextField(verbose_name='Comment Text', max_length=500)

    def __str__(self):
        return f'comment:{self.name}-{self.email} For {self.post.title}'
