from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save(commit=False)

        user.emailaddress_set.create(email=user.email, primary=True, verified=False)
        user.send_confirmation_mail(self.request)

        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return response


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


@login_required
class PasswordResetView(View):
    template_name = 'registration/password_reset_form.html'

    def post(self, request, *args, **kwargs):
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = get_user_model().objects.get(email=email)
            password = get_user_model().objects.make_random_password()
            user.set_password(password)
            user.save()

            subject = 'Пароль изменен'
            message = 'Ваш новый пароль: {password}'.format(password=password)

            from_email = user.email
            send_mail(subject, message, from_email, [user.email])

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return HttpResponseRedirect(reverse('password_reset_done'))
        return render(request, self.template_name, {'form': form})


@login_required
class UserPasswordResetDoneView(PasswordResetDoneView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/password_reset_done.html'
    success_url = reverse_lazy('users:password_reset_done')


@login_required
class UserPasswordResetConfirmView(PasswordResetConfirmView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_confirm')


@login_required
class UserPasswordResetCompleteView(PasswordResetCompleteView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/password_reset_done.html'
    success_url = reverse_lazy('users:password_reset_done')