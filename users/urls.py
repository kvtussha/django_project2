from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from users.views import (RegisterView, ProfileView, PasswordResetView, PasswordResetDoneView,
                         PasswordResetConfirmView, PasswordResetCompleteView, ConfirmRegister, CustomLogoutView,
                         )


app_name = 'users'

urlpatterns = [
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/confirm/', ConfirmRegister.as_view(), name='confirm_register'),
]