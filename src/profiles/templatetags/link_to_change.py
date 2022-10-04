from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
@mark_safe
def link_to_change(obj):
    app = obj._meta.app_label
    model = obj._meta.model.__name__.lower()
    url = 'http://127.0.0.1:8000/admin/{app}/{model}/{id}/change'.format(model=model, app=app, id=obj.id)
    return f'<a href="{url}">Link to edit object in admin</a>'
