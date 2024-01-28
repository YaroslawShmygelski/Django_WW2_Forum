from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from sitetest.models import Category, Country


@deconstructible
class Title_Validator:
    ALLOWED_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    code = "english"

    def __init__(self, message=None):
        self.message = message if message else "You are stupid"

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


class CreateForm(forms.Form):
    title = forms.CharField(max_length=255, label="Title", validators=[Title_Validator()])
    content = forms.CharField(widget=forms.Textarea())
    is_published = forms.BooleanField(required=False, label="Publish", initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Another Category")
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=False, empty_label="Not Listed")
