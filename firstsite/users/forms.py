from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Login", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'passsword']


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Create username", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Create password", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Repeat password", widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': "E-mail address",
            'first_name': "First name",
            'last_name': "Last name"
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'})
        }

        def clean_email(self):
            email_form = self.cleaned_data['email']
            if get_user_model().objects.filter(email=email_form).exists():
                raise forms.ValidationError("Email already taken")
            return email_form
