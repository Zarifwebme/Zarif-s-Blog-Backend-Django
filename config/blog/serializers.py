from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "title", "excerpt", "image_url", "created_at", "category"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if not obj.image_data:
            return None
        url = f"/media/post/{obj.id}/image/"
        return request.build_absolute_uri(url) if request else url


class PostDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "title", "description", "excerpt", "image_url", "created_at", "category"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if not obj.image_data:
            return None
        url = f"/media/post/{obj.id}/image/"
        return request.build_absolute_uri(url) if request else url
