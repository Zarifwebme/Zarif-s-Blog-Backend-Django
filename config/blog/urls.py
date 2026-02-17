from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PostViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="categories")
router.register("posts", PostViewSet, basename="posts")

urlpatterns = router.urls
