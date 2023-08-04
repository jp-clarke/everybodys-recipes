from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>', views.RecipeDetail.as_view(), name='recipe_detail'),
    path(
        'favourited/<slug:slug>',
        views.RecipeFavourite.as_view(),
        name='recipe_favourited'
    ),
    path(
        'comment_confirm_delete/<int:pk>',
        views.DeleteComment.as_view(),
        name='comment_confirm_delete'
    ),
    path(
        'comment_update_form/<int:pk>',
        views.EditComment.as_view(),
        name='comment_update_form'
    ),
    path(
        'create_recipe_form/',
        views.CreateRecipe.as_view(),
        name='create_recipe_form'
    ),
    path('favourites/', views.FavouritesList.as_view(), name='favourites'),
    path('my_recipes/', views.MyRecipesList.as_view(), name='my_recipes'),
]
