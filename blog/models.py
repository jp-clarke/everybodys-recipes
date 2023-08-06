from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_summernote.fields import SummernoteTextField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe_post'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    recipe_photo = CloudinaryField('image', default='placeholder')
    description = SummernoteTextField()
    ingredients = SummernoteTextField()
    instructions = SummernoteTextField()
    favourited = models.ManyToManyField(
        User, related_name='favourited_recipes', blank=True
    )
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

    def favourited_count(self):
        return self.favourited.count()


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments'
    )
    name = models.CharField(max_length=80)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    edited = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
