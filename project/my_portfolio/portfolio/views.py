from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, FormView


def home(request):
    return render(request, 'home.html')