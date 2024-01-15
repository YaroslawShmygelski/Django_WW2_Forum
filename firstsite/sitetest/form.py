from django import forms

from sitetest.models import Category, Country


class CreateForm(forms.Form):
    title = forms.CharField(max_length=255, label="Title")
    content = forms.CharField(widget=forms.Textarea())
    is_published=forms.BooleanField(required=False, label="Publish", initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Another Category")
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=False, empty_label="Not Listed")
