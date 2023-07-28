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
        name='comment_confirm_delete'),
    # path(
    #     'comment_confirm_delete/<int:pk>',
    #     views.DeleteComment.as_view(),
    #     name='comment_confirm_delete'),
]
