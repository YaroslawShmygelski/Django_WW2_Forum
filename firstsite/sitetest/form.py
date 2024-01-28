from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from sitetest.models import Category, Country, Persons


@deconstructible
class Title_Validator:
    ALLOWED_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    code = "english"

    def __init__(self, message=None):
        self.message = message if message else "You wrote bad title"

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


class CreateForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Another Category")

    class Meta:
        model = Persons
        fields = ['title','content', 'is_published', 'cat', 'tags']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-input', 'placeholder':"name of character only capital letters"}),
            'content': forms.Textarea(attrs={'rows':7, 'cols':50, 'placeholder':"Decribe your Character."})
        }
