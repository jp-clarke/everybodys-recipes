from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('date_created')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        # item = recipe.ingredients
        comments = recipe.comments.filter(approved=True).order_by('date_created')
        favourited = False
        if recipe.favourited.filter(id=self.request.user.id).exists():
            favourited = True

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                # 'item': item,
                'comments': comments,
                'favourited': favourited
            },
        )
