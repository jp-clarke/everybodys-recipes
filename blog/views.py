from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.text import slugify
from .models import Recipe, Comment
from .forms import (CommentForm, RecipeForm)


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-date_created')
    template_name = 'index.html'
    paginate_by = 9


class FavouritesList(generic.ListView):
    model = Recipe
    template_name = 'favourites.html'
    paginate_by = 9

    def get_queryset(self):
        return Recipe.objects.filter(
            status=1,
            favourited=self.request.user.id
            ).order_by('-date_created')


class MyRecipesList(generic.ListView):
    model = Recipe
    template_name = 'my_recipes.html'
    paginate_by = 9

    def get_queryset(self):
        return Recipe.objects.filter(
            status=1,
            author=self.request.user.id
            ).order_by('-date_created')


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('date_created')
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
            messages.success(request, 'Your comment is awaiting approval')
            return HttpResponseRedirect(request.path_info)
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


class DeleteComment(LoginRequiredMixin,
                    UserPassesTestMixin,
                    generic.DeleteView):
    model = Comment
    template_name = 'comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user.username == comment.name

    def get_success_url(self):
        recipe = self.object.recipe
        messages.success(self.request, 'Your comment has been deleted')
        return reverse_lazy('recipe_detail', args=[recipe.slug])


class EditComment(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Comment
    fields = ['body']
    template_name = 'comment_update_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user.username == comment.name

    def get_success_url(self):
        recipe = self.object.recipe
        messages.success(
            self.request,
            'Your comment has been edited and is awaiting approval'
        )
        return reverse_lazy('recipe_detail', args=[recipe.slug])

    def form_valid(self, form):
        form.instance.approved = False
        form.instance.edited = True
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class CreateRecipe(LoginRequiredMixin, generic.CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'create_recipe_form.html'
    success_url = '/my_recipes/'

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if (form.is_valid()):
            form.instance.author_id = request.user.id
            form.instance.slug = slugify(form.instance.title)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(
            self.request,
            'Your recipe has been uploaded and will\
             be published by the administrator'
        )
        return HttpResponseRedirect(self.get_success_url())
