django-myblog
=============

Blogging app for django

Configure Django
----------------

add to urls.py

```
(r'^', include('myblog.urls'))
```

settings.py

```
import os.path

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))  # get project path

APP_PATH = os.path.join(PROJECT_PATH, 'myblog')  # set app path

TEMPLATE_PATH = os.path.join(APP_PATH, 'templates')  # set templates path

BLOG_SETTINGS = {
  'general': {
    'blog_title': 'Blog Title',  # your blog title
    'blog_subtitle': 'Blog Subtitle',  # your blog subtitle
  },
  'appearance': {
    'theme': 'simple-clean',  # default theme
  },
  'reading': {
    'posts': 3,  # number of post displayed in home
  },
  'writing': {
    'publish': True,  # True = publish, False = draft
  },
  'comment': {
    'disqus': True,  # set to True using disqus
    'disqus_name': 'disqusname',  # your disqus username
  }
}

...

THEME_ROOT = os.path.join(TEMPLATE_PATH, BLOG_SETTINGS['appearance']['theme'])  # set used theme root

ASSETS_ROOT = os.path.join(THEME_ROOT, 'assets')  # set theme assets root

ASSETS_URL = '/assets/'  # set theme assets url

...

TEMPLATE_DIRS = (
  ...
  os.path.join(TEMPLATE_PATH, BLOG_SETTINGS['appearance']['theme']),
  ...
)

...

INSTALLED_APPS = (
  ...
  'myblog',
  ...
)
```

update database

```
python manage.py syncdb
```

First Use
