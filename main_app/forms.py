from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'prep_time', 'cook_time', 'ingredients', 'steps', 'optional_link', 'upload_file', 'checkboxes']
        widgets = {
            'checkboxes': forms.CheckboxSelectMultiple,
        }

def clean_checkboxes(self):
        selected_checkboxes = self.cleaned_data.get('checkboxes')
        if not selected_checkboxes:
            raise forms.ValidationError("Please select at least one checkbox.")
        elif len(selected_checkboxes) > 2:
            raise forms.ValidationError("Please select up to two checkboxes.")
        return selected_checkboxes
