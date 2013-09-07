from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext as _

import datetime

_PUBLISH_OPTIONS = (
  (0, _('Draft')),
  (1, _('Publish')),
)

class Author(User):
  class Meta:
    proxy = True

  def __unicode__(self):
    return '%s' % ' '.join([self.first_name, self.last_name])

  def get_absolute_url(self):
    return reverse('view_blog_author', args=[self.username])


class Category(models.Model):
  category = models.CharField(max_length=255, blank=False, null=False)
  slug = models.SlugField(_('slug'), max_length=255, unique=True)

  class Meta:
    verbose_name = _("category")
    verbose_name_plural = _("categories")

  def __unicode__(self):
    return '%s' % self.category

  @permalink
  def get_absolute_url(self):
    return ('view_blog_category', None, {'slug': self.slug})


class Post(models.Model):
  title = models.CharField(_('title'), max_length=255, blank=False, null=False)
  slug = models.SlugField(_('slug'), max_length=255, unique=True)
  content = models.TextField(_('content'), blank=False, null=False)
  author = models.ForeignKey(Author, blank=False, null=False)
  category = models.ForeignKey(Category, blank=False, null=False)
  status = models.BooleanField(_('status'), default=settings.BLOG_SETTINGS['writing']['publish'], choices=_PUBLISH_OPTIONS)
  date = models.DateTimeField(_('date'), default=datetime.date.today(), blank=False, null=False)

  class Meta:
    verbose_name = _("post")
    verbose_name_plural = _("posts")

  def __unicode__(self):
    return '%s' % self.title

  @permalink
  def get_absolute_url(self):
    return ('view_blog_post', None, {'slug': self.slug})

  def _unescape(self):
    return '%s' % self.content

  _unescape.allow_tags = True
