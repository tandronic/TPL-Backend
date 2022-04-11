from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class ArticleView(TemplateView):
    template_name = 'anunt.html'


class AboutUsView(TemplateView):
    template_name = 'despre.html'


class TicketsView(TemplateView):
    template_name = 'bilete.html'
