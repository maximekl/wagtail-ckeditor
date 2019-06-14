Wagtail CKEditor plugin
======

This is a [Wagtail](https://wagtail.io/) plugin, which allows [CKEditor](http://ckeditor.com/) to be used as an internal editor
instead of Draftail.js.

How to install
----
Include `wagtail2_ckeditor` in your `INSTALLED_APPS`.

Ensure that you have this entry in your `settings.py` file.


```python
    WAGTAILADMIN_RICH_TEXT_EDITORS = {
        'default': {
            'WIDGET': 'wagtail_ckeditor.widgets.CKEditor'
        }
    }
```
