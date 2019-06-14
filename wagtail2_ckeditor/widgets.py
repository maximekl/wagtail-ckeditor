from __future__ import absolute_import, unicode_literals

import json

from django.forms import widgets
from django.utils.safestring import mark_safe
from wagtail.utils.widgets import WidgetWithScript
from wagtail.admin.edit_handlers import RichTextFieldPanel
from wagtail2_ckeditor.utils import DbWhitelister, EditorHTMLConverter
# from wagtail.core.whitelist import Whitelister
from wagtail2_ckeditor import settings


class CKEditor(WidgetWithScript, widgets.Textarea):

    def get_panel(self):
        return RichTextFieldPanel

    def render(self, name, value, renderer, attrs=None):
        self.html_converter = EditorHTMLConverter()
        if value is None:
            translated_value = None
        else:
            html = value
            translated_value = self.html_converter.from_database_format(html)
        if attrs is None:
            attrs = {'id': 'wagtail2-ckeditor'}
        else:
            attrs['id'] = 'wagtail2-ckeditor'
        return super().render(name, translated_value, attrs, renderer)

    def render_js_init(self, editor_id, name, value):
        return "CKEDITOR.replace( '%s', %s);" % (editor_id, mark_safe(json.dumps(settings.WAGTAIL2_CKEDITOR_CONFIG)))

    def value_from_datadict(self, data, files, name):
        html = super().value_from_datadict(data, files, name)
        if html is None:
            return None
        self.html_converter = EditorHTMLConverter()
        return self.html_converter.to_database_format(html)
        #return DbWhitelister.clean(html)
