from django.views.generic import TemplateView

from route.models import Route


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class ArticleView(TemplateView):
    template_name = 'anunt.html'


class AboutUsView(TemplateView):
    template_name = 'despre.html'


class TicketsView(TemplateView):
    template_name = 'bilete.html'


class MapsView(TemplateView):
    template_name = 'harti.html'

    def get_context_data(self, **kwargs):
        context = super(MapsView, self).get_context_data(**kwargs)
        context['routes'] = Route.objects.all()
        return context
