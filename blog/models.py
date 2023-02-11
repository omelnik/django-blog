from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT     = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    class PublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=Post.Status.PUBLISHED)

    title     = models.CharField(max_length=250)
    slug      = models.CharField(max_length=250)
    author    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body      = models.TextField()
    publish   = models.DateTimeField(default=timezone.now)
    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)
    status    = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objectes  = models.Manager()
    published = PublishedManager()

    class Meta:
        indexes  = [models.Index(fields=['-publish'])]
        ordering = ['-publish']

    def __str__(self) -> str:
        return self.title