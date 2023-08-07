from django import forms
from .models import Recipe, CuttingBoard

class RecipeForm(forms.ModelForm):
    OPTIONS_CHOICES = [
        ('Vegetarian', 'Vegetarian'),
        ('Dairy-Free', 'Dairy-Free'),
        ('Beef', 'Beef'),
        ('Pork', 'Pork'),
        ('Chicken', 'Chicken'),
    ]

    checkboxes = forms.MultipleChoiceField(
        choices=OPTIONS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(RecipeForm, self).__init__(*args, **kwargs)

        if self.user:
            if not self.instance.user == self.user:
                self.fields["optional_link"].widget = forms.HiddenInput()

    class Meta:
        model = Recipe
        fields = [
            "title",
            "prep_time",
            "cook_time",
            "ingredients",
            "steps",
            "optional_link",
            "upload_file",
            "checkboxes",
            "difficulty",
        ]
        widgets = {
            "checkboxes": forms.CheckboxSelectMultiple,
        }


class CuttingBoardForm(forms.ModelForm):
    class Meta:
        model = CuttingBoard
        fields = ["title", "description"]