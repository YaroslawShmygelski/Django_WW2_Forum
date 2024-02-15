import django.contrib.auth.views as auth_view
from django.urls import path, reverse_lazy
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('logout/', auth_view.LogoutView.as_view(), name="logout"),
    path('register/', views.UserRegisterView.as_view(), name="registration"),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('password-change/', views.UserPasswordChangeView.as_view(), name='password-change'),

    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset_form.html',
                                                                email_template_name='users/user_password_reset_email.html',
                                                                success_url=reverse_lazy('users:password_reset_done')),
         name='password_reset'),
    path('password_reset/done/',
         auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                                    success_url=reverse_lazy('users:password_reset_complete')),
         name='password_reset_confirm'),
    path('accounts/reset/done//',
         auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

]
