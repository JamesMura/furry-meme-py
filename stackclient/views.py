from django.views.generic import TemplateView, FormView

from stackclient.forms import UserRegistrationForm


class HomeView(TemplateView):
    template_name = "home.html"


class RegisterView(FormView):
    template_name = "register.html"
    form_class = UserRegistrationForm
    success_url = "/"

    def form_valid(self, form):
        # add logic to create user
        return super(RegisterView, self).form_valid(form)