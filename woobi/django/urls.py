from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'pb/', views.postback_handler, name='woobi-postback'),
]
