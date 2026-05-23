from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category

def get_published_posts():
    return Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )

def index(request):
    post_list = get_published_posts().order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)

def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = get_published_posts().filter(
        category=category
    ).order_by('-pub_date')
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(
        get_published_posts(),
        pk=post_id
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
