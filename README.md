# Arquivo

## Preparando o ambiente de desenvolvimento

1. Instalar poetry: `$ python3 -m pip install poetry`
2. Instale nodejs e npm
3. Utilize o poetry para criar o ambiente virtual python: `$ poetry install`
4. Utilize npm para instalar as dependencias para gerar o CSS: `$ npm install`
5. Inicialize um projeto Django: `$ poetry run django-admin startproject config .`
6. Edite `config\settings.py` conforme abaixo:

```python
INSTALLED_APPS = [
    ...
    "widget_tweaks",
    "arquivo",
]

# Opcional, mas recomendado para ambiente de desenvolvimento
if DEBUG:
    INSTALLED_APPS += [
        "django_extensions",
        "debug_toolbar",
        "livereload",
    ]
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        "livereload.middleware.LiveReloadScript",
    ]

TEMPLATES = [
    {
        # ...
        "OPTIONS": {
            "context_processors": [
                # ...
                "arquivo.context_processors.arquivo",
            ],
        },
    },
]

```

7. Adicione as urls do app em `config\urls.py`

```python
urlpatterns = [
    path("", include("arquivo.urls")),
    path("admin/", admin.site.urls),
]

# Inclua também as urls do debug_toolbar se adicionou o app em settings.py
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]

```

## Executando o ambiente de desenvolvimento

### Servidor Django

Usando o servidor padrão do django:

```bash
$ poetry run python manage.py runserver
```

Ou usando o Werkzeug com o django_extensions:

```bash
$ poetry run python manage.py runserver_plus --keep-meta-shutdown
```

### Servidor livereload

O livereload oferece a comodidade de automaticamente recarregar as páginas no navegador sempre que detectar alteração no projeto.

```bash
poetry run python manage.py livereload
```

### Processador CSS para tailwindcss

O CSS do app precisa ser gerado utilizando o tailwindcss.

```bash
npx tailwindcss -i arquivo/static/arquivo/base.css -o arquivo/static/arquivo/style.css --watch
```


### Configurando o login do sistema
1 - Incluir no config/settings.py:
```python
LOGIN_URL = "/accounts/login/"
```
2 - Incluir no config/urls.py:
```python
from django.contrib.auth import views as auth_views
...
urlpatterns = [
...
    path("accounts/login/", auth_views.LoginView.as_view(next_page="/", redirect_field_name="next"),name="login",),
    path("accounts/logout", auth_views.LogoutView.as_view(next_page="login"), name="logout",),
...
]
...

```

