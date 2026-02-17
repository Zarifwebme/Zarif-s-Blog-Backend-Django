from rest_framework import viewsets
from .models import Category, Post
from .serializers import CategorySerializer, PostListSerializer, PostDetailSerializer
from .permissions import ReadOnly
from rest_framework.filters import SearchFilter


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ReadOnly]

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ["title", "description"]
    permission_classes = [ReadOnly]

    def get_queryset(self):
        qs = (
            Post.objects
            .filter(is_published=True)
            .select_related("category")
            .order_by("-id")
        )

        category_slug = self.request.query_params.get("category")
        if category_slug:
            qs = qs.filter(category__slug=category_slug)

        return qs

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostDetailSerializer
        return PostListSerializer

