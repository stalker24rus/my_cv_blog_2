from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

from ckeditor.fields import RichTextField



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    def __str__(self):
        return f'Profile for user {self.user.username}'


class Image(models.Model):
     title = models.CharField(max_length=200)
     image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True )  # /%m/%d removed

     def __str__(self):
         return self.title


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
            .filter(status='published')


# Create your models here.
class Post(models.Model):
    """The post model """
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    objects = models.Manager()  # The default manager
    published = PublishedManager()  # Our custom manager

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.author,
                             self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


# check git commits
class Comment(models.Model):
    """The comment models"""
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

