from django.views.generic.base import TemplateView
from wagtail2_ckeditor import settings


class IndexView(TemplateView):
    template_name = "wagtail2_ckeditor/index.html"

    def get_context_data(self, **kwargs):
        data = super(IndexView, self).get_context_data(**kwargs)
        data["use_math"] = settings.WAGTAIL2_CKEDITOR_USE_MATH
        data["ckeditor_config"] = settings.JSON_CONFIG
        data["mathjax_url"] = settings.WAGTAIL2_CKEDITOR_MATHJAX_URL
        return data
