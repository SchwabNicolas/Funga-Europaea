from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from authentication.models import FEUser
from authentication.forms import FEUserCreationForm

# Create your views here.
class FESignUpView(CreateView):
    """
    Sign up view.
    """

    form_class = FEUserCreationForm
    success_url = reverse_lazy('core:index')
    template_name = 'authentication/signup.html'
    success_message = 'Successfully created your account.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sign up'
        context['description'] = 'Sign up in Funga Europaea.'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        if 'next' in self.request.GET:
            response = redirect(self.request.GET.get('next'))
        return response
