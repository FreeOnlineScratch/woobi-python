from hashlib import md5

from requests.exceptions import HTTPError as rHTTPError
import requests
import six


API_PATH = 'https://api.woobi.com/TAS/v1/offers'


class HTTPError(Exception):
    pass


def api(hash_value=None, secret_key=None, custom_params={}, **kwargs):
    """
    kwargs:
        - application_id
        - client_id
        - client_ip
        - user_state
        - user_level
        - user_agent

    optional kwargs:
        - gender
        - age
        - age_group

    http://woobi.com/support-2/#!articles/163-1021-api-requests
    """
    uri = '{}'
    params = dict(
        aid=kwargs.pop('application_id'),
        cid=kwargs.pop('client_id'),
        ip=kwargs.pop('client_ip'),
        usrStat=kwargs.pop('user_state'),
        level=kwargs.pop('user_level'),
        userAgent=kwargs.pop('user_agent'),
    )

    optional = ('gender', 'age', 'age_group',)
    for k, v in kwargs.items():
        if k in optional and v:
            params[k] = v

    for k, v in custom_params.items():
        if not k.startswith('_'):
            k = '_{}'.format(k)
        if v:
            params[k] = v

    if hash_value and secret_key:
        hash = md5()
        hash.update(hash_value + secret_key)
        params['hv'] = hash_value
        params['hs'] = hash.hexdigest()


    r = requests.get(API_PATH, data=params, headers={'Accept': 'application/json'})
    try:
        r.raise_for_status()
    except rHTTPError as e:
        six.reraise(HTTPError, e)

    return r.json()
