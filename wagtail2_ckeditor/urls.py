from django.conf.urls import url
from django.views.generic import TemplateView

from wagtail2_ckeditor.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
]
