from django.contrib import admin
from django import forms
from .models import Category, Post

class PostAdminForm(forms.ModelForm):
    image_upload = forms.ImageField(required=False, label="Post rasmi")

    class Meta:
        model = Post
        fields = "__all__"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm  # 🔥 yangi form ishlatiladi
    list_display = ("title", "category", "created_at", "is_published")
    list_filter = ("category", "is_published", "created_at")
    search_fields = ("title", "description", "excerpt")
    ordering = ("-created_at",)

    def save_model(self, request, obj, form, change):
        img = form.cleaned_data.get("image_upload")

        if img:
            obj.image_name = img.name
            obj.image_content_type = getattr(img, "content_type", "application/octet-stream")
            obj.image_data = img.read()  # bytes -> Postgres

        super().save_model(request, obj, form, change)
