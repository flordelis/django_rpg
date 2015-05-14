from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

"""
Everything I do, I do to make forms crispier.
"""

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            ButtonHolder(
                Submit('login', 'Login', css_class='btn-primary')
            )
        )


class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password1',
            'password2',
            ButtonHolder(
                Submit('register', 'Register', css_class='btn-primary')
            )
        )


class ChangePasswordForm(PasswordChangeForm):

    def __init__(self, user, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(user, *args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'old_password',
            'new_password1',
            'new_password2',
            ButtonHolder(
                Submit('submit', 'Change Password', css_class='btn-primary')
            )
        )


class ForgotPasswordForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(ForgotPasswordForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'email',
            ButtonHolder(
                Submit('submit', 'Send Recovery Email', css_class='btn-primary')
            )
        )