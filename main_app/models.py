from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def get_default_user():
    return User.objects.first().id if User.objects.exists() else None

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    title = models.CharField(max_length=100)
    prep_time = models.CharField(max_length=50)
    cook_time = models.CharField(max_length=100, default='Unspecified')
    ingredients = models.TextField()
    steps = models.TextField()
    optional_link = models.URLField(blank=True)
    upload_file = models.FileField(upload_to='recipe_uploads/', blank=True)
    difficulty = models.CharField(max_length=100, default='Unspecified')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    cutting_boards = models.ManyToManyField('CuttingBoard', blank=True)

    CHECKBOX_CHOICES = (
        ('Vegetarian', 'Vegetarian'),
        ('Dairy-Free', 'Dairy-Free'),
        ('Beef', 'Beef'),
        ('Pork', 'Pork'),
        ('Chicken', 'Chicken'),
    )
    
    checkboxes = models.CharField(max_length=100, choices=CHECKBOX_CHOICES, blank=True)

    def __str__(self):
        return self.title


class CuttingBoard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
