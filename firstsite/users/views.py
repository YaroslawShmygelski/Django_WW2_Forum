from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from firstsite import settings
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserPasswordChangeForm


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

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {'title': "Login"}



class UserRegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    extra_context = {'title': "Registration"}
    success_url = reverse_lazy('users:login')

# def register_user(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return render(request, 'users/register_done.html')
#     else:
#         form = RegistrationForm()
#     return render(request, 'users/register.html', context={'form': form})


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = 'users/user_profile.html'
    extra_context = {'title': "Profile",
                     'default_photo': settings.DEFAULT_PROFILE_PHOTO}

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('users:profile')
    title = "Password Change"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Password Successfully Changed')
        return response
