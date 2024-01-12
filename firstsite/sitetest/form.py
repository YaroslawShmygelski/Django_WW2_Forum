from django import forms

from sitetest.models import Category, Country


class CreateForm(forms.Form):
    title = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea())
    cat = forms.ModelChoiceField(queryset=Category.objects.all())
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=False)
