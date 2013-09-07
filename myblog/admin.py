from django import forms
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

  def save_model(self, request, obj, form, change):
    if not change:
      obj.author = request.user
    obj.save()


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
