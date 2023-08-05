from crispy_forms.helper import FormHelper
from .models import Comment, Recipe
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
        fields = (
            'title',
            'recipe_photo',
            'description',
            'ingredients',
            'instructions',
        )


# IngredientsFormSet = inlineformset_factory(
#     Recipe, Ingredients, fields=('amount', 'ingredient',), extra=2
# )
# InstructionsFormSet = inlineformset_factory(
#     Recipe, Instructions, fields=('steps',), extra=1
# )
