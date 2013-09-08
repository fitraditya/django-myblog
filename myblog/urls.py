from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from myblog.views import index

urlpatterns = patterns('',
  url(r'^$', 'myblog.views.index'),
  url(r'^assets/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.ASSETS_ROOT}),
  url(r'^plugins/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.PLUGINS_ROOT}),
  url(r'^view/(?P<slug>[^\.]+)', 'myblog.views.view_post', name='view_blog_post'),
  url(r'^category/(?P<slug>[^\.]+)', 'myblog.views.view_category', name='view_blog_category'),
  url(r'^author/(?P<author>[^\.]+)', 'myblog.views.view_author', name='view_blog_author'),
)
