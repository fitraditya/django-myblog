from django.conf import settings
from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from myblog.models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('category',)}


class PostAdmin(admin.ModelAdmin):
  exclude = ['author', 'date']
  date_hierarchy = 'date'
  list_display = ('title', 'author', 'date', 'status')
  list_filter = ['author', 'category', 'status']
  search_fields = ('title', 'body')
  prepopulated_fields = {'slug': ('title',)}
  formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'size':'140'})},
    models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':100})},
  }

  class Media:
    js = [ settings.ASSETS_URL+'js/tinymce/tiny_mce.js', settings.ASSETS_URL+'js/run_tinymce.js' ]

  def save_model(self, request, obj, form, change):
    if not change:
      obj.author = request.user
    obj.save()


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
