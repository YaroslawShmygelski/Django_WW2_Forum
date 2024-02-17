from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'passsword']


class UserRegistrationForm(UserCreationForm):
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


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(label="Change Username", widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label="Change Username",
                            widget=forms.TextInput(attrs={'class': 'form-input'}))
    class Meta:
        model = get_user_model()
        fields = ['photo', 'username', 'email', 'first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'photo':forms.FileInput()
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Current Password", widget=forms.TextInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="New Password", widget=forms.TextInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Confirm new Password", widget=forms.TextInput(attrs={'class': 'form-input'}))
