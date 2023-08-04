from crispy_forms.helper import FormHelper
from .models import Comment, Recipe, Ingredients, Instructions
from django import forms
from django.forms import inlineformset_factory


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': ""}
        label_suffix = ''


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'recipe_photo', 'description',)


IngredientsFormSet = inlineformset_factory(
    Recipe, Ingredients, fields=('amount', 'ingredient',), extra=1
)
InstructionsFormSet = inlineformset_factory(
    Recipe, Instructions, fields=('steps',), extra=1
)
