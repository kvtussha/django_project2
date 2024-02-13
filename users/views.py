from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, \
    PasswordResetView
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView, UpdateView

from users.forms import UserProfileForm, UserRegistrationForm
from users.models import User


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()

        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')

        return response


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    success_url = reverse_lazy('users:password-reset')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Отправка подтверждающего письма
        email = form.cleaned_data['email']
        user = get_user_model().objects.get(email=email)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        subject = 'Сброс пароля'
        message = 'Чтобы завершить сброс пароля, перейдите по ссылке: {url}'.format(
            url=self.request.build_absolute_uri(
                reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            )
        )
        from_email = 'skystore@gmail.com'
        send_mail(subject, message, from_email, [user.email])

        return response

    def get_success_url(self):
        return reverse('password_reset_done')


class UserPasswordResetDoneView(LoginRequiredMixin, PasswordResetDoneView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/password_reset_done.html'
    success_url = reverse_lazy('users:password_reset_done')


class UserPasswordResetConfirmView(LoginRequiredMixin, PasswordResetConfirmView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_confirm')


class UserPasswordResetCompleteView(LoginRequiredMixin, PasswordResetCompleteView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/password_reset_done.html'
    success_url = reverse_lazy('users:password_reset_done')
