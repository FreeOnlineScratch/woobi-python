from woobi import API_PATH

from django.conf import settings

def postback_handler(req):
    client_id = req.GET['client_id']
