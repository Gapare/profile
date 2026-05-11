from django.shortcuts import render, get_object_or_404
from .models import Post, Tag

def blog_home(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    tags = Tag.objects.all()
    return render(request, 'blog/blog_home.html', {
        'posts': posts,
        'tags': tags
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    related_posts = Post.objects.filter(
        tags__in=post.tags.all(),
        is_published=True
    ).exclude(id=post.id).distinct()[:3]
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'related_posts': related_posts
    })

def posts_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags=tag, is_published=True).order_by('-created_at')
    return render(request, 'blog/blog_home.html', {
        'posts': posts,
        'tag': tag,
        'tags': Tag.objects.all()
    })