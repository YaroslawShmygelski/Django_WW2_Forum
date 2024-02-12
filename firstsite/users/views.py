from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from users.forms import LoginForm, RegistrationForm


# Create your views here.
# def login_users(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'],
#                                 password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#     else:
#         form = LoginForm()
#
#     return render(request, 'users/login.html', {'form': form})

class LoginUsers(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    # def get_success_url(self):
    #     return reverse_lazy('home')


#
# def logout_users(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('users:login'))


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'users/register_done.html')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', context={'form': form})
