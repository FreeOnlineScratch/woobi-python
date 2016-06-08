# Woobi API

```python
from woobi import api as woobi_api

woobi_api(application_id=APP_ID,
          client_id=CLIENT_ID,
          user_state='user state',
          user_level='user level',
          user_agent='Mozilla ...',
          custom_params={})
```

Optional arguments: `age`, `age_group`, `gender`. Passing `hash_value` and `secret_key` will enable signing of the request.

## Django integration

### Settings

Add to `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    'woobi.django',
)
```

Add to `TEMPLATES`:

```python
TEMPLATES = [
    'OPTIONS': dict(
        context_processors=[
            'woobi.django.context_processors.all'
        ],
    ),
]
```

Add your application ID and secret key:

```python
from woobi.django.settings import *
WOOBI_APP_ID = 'something'
WOOBI_APP_SECRET_KEY = 'hash value'
```

See [`settings.py`](woobi/django/settings.py)

### URLs

In your own `urls.py`:

```python
urlpatterns += [
    url(r'^woobi/', include('woobi.django.urls')),
]
```

Use `woobi-postback` to reference the postback path. Note that `woobi.django.views.postback_handler` is the most incomplete part of this project.

### Templating

```jinja2
{% load woobi %}

<!DOCTYPE html>
<html>
    <head>
        {# May want this after all other stylesheets #}
        {% include 'woobi_css.html.j2' %}
    </head>

    <body>
        {# After jQuery #}
        {% woobi_javascript %}
    </body>
</html>
```
