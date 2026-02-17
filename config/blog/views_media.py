from django.http import Http404, HttpResponse
from .models import Post


def post_image(request, pk: int):
    try:
        post = Post.objects.get(pk=pk, is_published=True)
    except Post.DoesNotExist:
        raise Http404("Post not found")

    if not post.image_data:
        raise Http404("Image not found")

    content_type = post.image_content_type or "application/octet-stream"
    resp = HttpResponse(post.image_data, content_type=content_type)

    if post.image_name:
        resp["Content-Disposition"] = f'inline; filename="{post.image_name}"'
    return resp
