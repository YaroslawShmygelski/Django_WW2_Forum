from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Login", widget=forms.TextInput(attrs = {'class': 'form-input'}))
    password=forms.CharField(label='Password', widget=forms.PasswordInput(attrs = {'class': 'form-input'}))
