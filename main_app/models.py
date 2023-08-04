from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    prep_time = models.CharField(max_length=100)
    ingredients = models.TextField()
    steps = models.TextField()
    optional_link = models.URLField(blank=True)
    upload_file = models.FileField(upload_to='recipe_uploads/', blank=True)

    updated_at = models.DateTimeField(auto_now=True)


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
