from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="posts")
    title = models.CharField(max_length=200)
    description = models.TextField()
    excerpt = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    image_data = models.BinaryField(blank=True, null=True, editable=False)
    image_name = models.CharField(max_length=255, blank=True, null=True, editable=False)
    image_content_type = models.CharField(max_length=100, blank=True, null=True, editable=False)

    def __str__(self):
        return self.title
