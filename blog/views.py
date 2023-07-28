from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Recipe, Comment
from .forms import CommentForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('date_created')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(
            approved=True).order_by('date_created')
        favourited = False
        if recipe.favourited.filter(id=self.request.user.id).exists():
            favourited = True

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'commented': False,
                'favourited': favourited,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(
            approved=True).order_by('date_created')
        favourited = False
        if recipe.favourited.filter(id=self.request.user.id).exists():
            favourited = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'commented': True,
                'favourited': favourited,
                'comment_form': CommentForm()
            },
        )


class RecipeFavourite(View):

    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.favourited.filter(id=request.user.id).exists():
            recipe.favourited.remove(request.user)
        else:
            recipe.favourited.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class DeleteComment(generic.DeleteView):
    model = Comment

    def get_success_url(self):
        recipe = self.object.recipe
        return reverse_lazy('recipe_detail', args=[recipe.slug])
