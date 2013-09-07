from django.conf import settings
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from myblog.models import Post, Category, Author

def index(request):
  return render_to_response('index.html', {
    'blog_title': settings.BLOG_SETTINGS['general']['blog_title'],
    'blog_subtitle': settings.BLOG_SETTINGS['general']['blog_subtitle'],
    'categories': Category.objects.all(),
    'posts': Post.objects.filter(status=True)[:settings.BLOG_SETTINGS['reading']['posts']]
  })


def view_post(request, slug):
  return render_to_response('view.html', {
    'post': get_object_or_404(Post, slug=slug)
  })


def view_category(request, slug):
  category = get_object_or_404(Category, slug=slug)

  return render_to_response('category.html', {
    'category': category,
    'posts': Post.objects.filter(category=category)[:settings.BLOG_SETTINGS['reading']['posts']]
  })


def view_author(request, author):
  author = get_object_or_404(Author, username=author)

  return render_to_response('author.html', {
    'author': author,
    'posts': Post.objects.filter(author=author)[:settings.BLOG_SETTINGS['reading']['posts']]
  }, context_instance=RequestContext(request))
