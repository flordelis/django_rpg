from forms import LoginForm, RegistrationForm, ChangePasswordForm
from forms import ForgotPasswordForm
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import password_reset


class RegisterView(generic.CreateView):

    form_class = RegistrationForm
    model = User
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        # set these so that we can login the user later? This probably isn't
        # the best way to do this?
        self.username = form.cleaned_data['username']
        self.password = form.cleaned_data['password1']
        return super(RegisterView, self).form_valid(form)

    def get_success_url(self):
        """
        This gets called after the object is created, so we should be safe to
        login a user now
        """
        user = authenticate(username=self.username, password=self.password)
        login(self.request, user)
        return super(RegisterView, self).get_success_url()



