from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'prep_time',
            'ingredients',
            'steps',
            'optional_link',
            'upload_file',
            'checkboxes',
        ]
