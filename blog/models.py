from django.db import models
from django.contrib.auth.models import User
# from ordered_model.models import OrderedModel
# from django_jsonform.models.fields import ArrayField
# https://django-jsonform.readthedocs.io/en/latest/
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe_post'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    recipe_photo = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    favourited = models.ManyToManyField(
        User, related_name='favourited_recipes', blank=True
    )
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def favourited_count(self):
        return self.favourited.count()


class Ingredients(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='ingredients'
    )
    amount = models.CharField(max_length=50)
    ingredient = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        return self.ingredient


class Instructions(models.Model):
    recipe = models.OneToOneField(
        Recipe, on_delete=models.CASCADE, related_name="instructions"
    )
    steps = models.TextField()

    def __str__(self):
        return self.steps


# class InstructionThroughModel(OrderedModel):
#     recipe = models.ForeignKey(
#         Recipe, on_delete=models.CASCADE
#     )
#     step = models.ForeignKey(
#         Instruction, on_delete=models.CASCADE
#     )
#     order_with_respect_to = 'step'

# #     class Meta:
# #         ordering = ('step', 'order')


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments'
    )
    name = models.CharField(max_length=80)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
