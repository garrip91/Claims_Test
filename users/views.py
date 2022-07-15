from django.views.generic import FormView, TemplateView

from users.forms import RegistrationForm


class RegistrationView(FormView):
    template_name = 'users/registration.html'
    success_url = '/thanks'
    form_class = RegistrationForm


class ThanksView(TemplateView):
    template_name = 'users/thanks.html'
