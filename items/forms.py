from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item

        fields = [
            "category",
            "title",
            "price",
            "description",
            "image",
            "status"
        ]

        widgets = {

            "category": forms.Select(attrs={
                "class": "form-select"
            }),

            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "price": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4
            }),

            "image": forms.FileInput(attrs={
                "class": "form-control"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

        }