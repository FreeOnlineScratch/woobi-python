import json

from django.conf import settings
from django.utils.html import escapejs
from django.utils.safestring import mark_safe

__all__ = [
    'assets',
    'config_js',
    'debug_js',
    'all',
]

def assets(req):
    css_uri = settings.WOOBI_VIDGET_CSS_URI
    js_uri = settings.WOOBI_VIDGET_JS_URI

    if settings.WOOBI_VIDGET_FORCE_MOBILE:
        css_uri = settings.WOOBI_VIDGET_MOBILE_CSS_URI
        js_uri = settings.WOOBI_VIDGET_MOBILE_JS_URI

    return {
        'woobi_css_uri': mark_safe(css_uri),
        'woobi_js_uri': mark_safe(js_uri),
        'woobi_mobile_css_uri': mark_safe(settings.WOOBI_VIDGET_MOBILE_CSS_URI),
        'woobi_mobile_js_uri': mark_safe(settings.WOOBI_VIDGET_MOBILE_JS_URI),
    }


def config_js(req):
    custom = ''
    if settings.WOOBI_CONFIG['customParams']:
        custom = '&'.join(['{}={}'.format(x, escapejs(y))
                          for x, y in
                          settings.WOOBI_CONFIG['customParams'].items()])

    view = json.dumps(settings.WOOBI_CONFIG['view']) if settings.WOOBI_CONFIG['view'] else '{}'

    return {
        'woobi_appId': mark_safe(settings.WOOBI_APP_ID),
        'woobi_customParams': mark_safe(custom),
        'woobi_view': mark_safe(view),
    }


def all(r):
    orig = assets(r)
    for k, v in config_js(r).items():
        orig[k] = v
    return orig
