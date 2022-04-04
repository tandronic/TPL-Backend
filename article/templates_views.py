from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class LoginTemplateView(TemplateView):
    template_name = 'register.html'

