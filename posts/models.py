import re

from django.conf import settings
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.template.defaultfilters import slugify

from core.models import UserProfile


# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "draft"),
        ("inprogress", "in progress"),
        ("published", "published")
    )

    author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    title      = models.CharField(max_length=200)
    slug       = models.SlugField(default="", unique=True)
    content    = models.TextField(blank=True, default="")
    word_count = models.IntegerField(blank=True, default=0)
    active     = models.BooleanField(default=False)
    status     = models.CharField(choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        text = re.sub("<[^>]*>", "", self.content).replace("&nbsp;", " ")
        self.word_count = len(re.findall(r"\b\w+\b", text))

        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
