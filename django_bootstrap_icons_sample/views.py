from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "django_bootstrap_icons_sample/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
