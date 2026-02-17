from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    image = serializers.ImageField()

    class Meta:
        model = Post
        fields = ["id", "title", "excerpt", "image", "created_at", "category"]


class PostDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    image = serializers.ImageField()

    class Meta:
        model = Post
        fields = ["id", "title", "description", "excerpt", "image", "created_at", "category"]
