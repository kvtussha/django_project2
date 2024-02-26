import random

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, \
    PasswordResetView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView, UpdateView, TemplateView

from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('main_app:product-list')

    def form_valid(self, form):

        user = form.save()

        current_site = self.request.get_host()
        subject = 'Подтверждение регистрации'

        verification_code = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        user.verification_code = verification_code

        user.save()

        message = render_to_string('registration/activation_email.html', {
            'user': user,
            'domain': current_site,
            'verification_code': verification_code
        })

        send_mail(subject, message, from_email=settings.EMAIL_HOST_USER, recipient_list=[user.email])

        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('main:product-list')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ConfirmRegister(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/register_done.html')

    @staticmethod
    def post(request, *args, **kwargs):
        token = int(request.POST.get('verification_code'))
        user = get_object_or_404(User, verification_code=token)

        if not user.is_active:
            user.is_active = True
            user.save()
            return redirect('users:login')
        return redirect('main_app:product-list')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    success_url = reverse_lazy('users:password_reset_done')
    form_class = PasswordResetForm

    def form_valid(self, form):
        # response = super().form_valid(form)

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

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:password-reset')


class UserPasswordResetDoneView(LoginRequiredMixin, PasswordResetDoneView):
    model = User
    form_class = UserRegisterForm
    template_name = 'registration/password_reset_done.html'
    success_url = reverse_lazy('users:password_reset_done')


class UserPasswordResetConfirmView(LoginRequiredMixin, PasswordResetConfirmView):
    model = User
    form_class = UserRegisterForm
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_confirm')

    @staticmethod
    def set_password(user):
        new_password = get_random_string(length=12)
        user.set_password(new_password)
        user.save()


class UserPasswordResetCompleteView(LoginRequiredMixin, PasswordResetCompleteView):
    model = User
    form_class = UserRegisterForm
    template_name = 'registration/password_reset_done.html'
    success_url = reverse_lazy('users:password_reset_done')

