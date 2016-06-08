import json

from django.conf import settings
from django.utils.html import escapejs


__all__ = [
    'WOOBI_APP_ID',
    'WOOBI_CONFIG',
    'WOOBI_VIDGET_CSS_URI',
    'WOOBI_VIDGET_FORCE_MOBILE',
    'WOOBI_VIDGET_MOBILE_JS_URI',
    'WOOBI_VIDGET_JS_URI',
    'WOOBI_VIDGET_MOBILE_CSS_URI',
]

WOOBI_APP_ID = None
WOOBI_APP_SECRET_KEY = None
WOOBI_APP_SIGN_REQUESTS = True

# http://woobi.com/support-2/#!articles/163-964-intro
WOOBI_VIDGET_CSS_URI = getattr(settings,
                               'WOOBI_VIDGET_CSS_URI',
                               '//products.woobi.com/vidget/vidget.css')
WOOBI_VIDGET_JS_URI = getattr(settings,
                              'WOOBI_VIDGET_JS_URI',
                              '//products.woobi.com/vidget/woobi-min.js')
WOOBI_VIDGET_MOBILE_CSS_URI = getattr(settings,
                                      'WOOBI_VIDGET_MOBILE_CSS_URI',
                                      '//products.woobi.com/vidget/vidget_mobile.css')
WOOBI_VIDGET_MOBILE_JS_URI = getattr(settings,
                                     'WOOBI_VIDGET_MOBILE_JS_URI',
                                     '//products.woobi.com/vidget/woobi_mobile-min.js')
WOOBI_VIDGET_FORCE_MOBILE = getattr(settings,
                                    'WOOBI_VIDGET_FORCE_MOBILE',
                                    False)
WOOBI_CONFIG = getattr(settings, 'WOOBI_CONFIG', dict(
    customParams={},
    view=dict(
        draggable=True,
        colorTheme='#db4e56',
        showTitle=True,
        showFooter=True,
        showCloseButton=True,
        showCounter=True,
        #backColor=None,
        #fontColor=None,
    ),
))

if WOOBI_VIDGET_FORCE_MOBILE:
    WOOBI_VIDGET_CSS_URI = WOOBI_VIDGET_MOBILE_CSS_URI
    WOOBI_VIDGET_JS_URI = WOOBI_VIDGET_MOBILE_JS_URI
