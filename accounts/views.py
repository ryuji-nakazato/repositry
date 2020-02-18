from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from accounts import forms
from .forms import MyPasswordChangeForm
from django.urls import reverse_lazy


class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "accounts/login.html"


class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "accounts/logout.html"


class IndexView(TemplateView):
    template_name = "accounts/index.html"


class PasswordChange(PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = "accounts/password_change.html"


class PasswordChangeDone(PasswordChangeDoneView):
    """パスワード変更しました"""
    template_name = "accounts/password_change_done.html"

