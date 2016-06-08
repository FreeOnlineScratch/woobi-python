from django import template
from django.template.loader import get_template
from django.utils.safestring import mark_safe
register = template.Library()

from ..context_processors import all as woobi_vars


@register.simple_tag
def woobi_javascript(client_id=None):
    tpl = get_template('woobi_js.html.j2')
    context = woobi_vars(None)
    context['woobi_clientId'] = mark_safe(client_id if client_id else 'not a valid client ID')

    return tpl.render(context)
