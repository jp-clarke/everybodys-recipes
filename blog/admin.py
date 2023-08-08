from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.admin import SummernoteInlineModelAdmin
''' https://github.com/summernote/django-summernote/issues/38 '''


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'date_created')
    list_display = ('id', 'title', 'slug', 'author', 'status', 'date_created')
    search_fields = ['title', ]
    summernote_fields = ('description', 'ingredients', 'instructions')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'body', 'recipe', 'date_created', 'approved')
    list_filter = ('approved', 'date_created')
    search_filter = ('name', 'body', 'recipe')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
