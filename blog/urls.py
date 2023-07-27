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
]
