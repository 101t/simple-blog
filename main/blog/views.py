from django.shortcuts import render, get_object_or_404

from .models import Post
def home_view(request):
    posts = Post.objects.filter(is_active=True)
    return render(request, "home.html", dict(posts=posts))

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "detail.html", dict(post=post))