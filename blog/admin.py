from django.contrib import admin
from .models import Recipe, Ingredient, Instruction, Comment
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.admin import SummernoteInlineModelAdmin
''' https://github.com/summernote/django-summernote/issues/38 '''


class IngredientInline(admin.TabularInline):

    model = Ingredient
    extra = 1


class InstructionInline(admin.TabularInline, SummernoteInlineModelAdmin):

    summernote_fields = ('step')
    model = Instruction
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
    inlines = (
        IngredientInline,
        InstructionInline,
    )


admin.site.register(Comment)
