# AX3 Redactor

This app is part of the AX3 technology developed by Axiacore.

It allows you to use Redactor within the Django admin interface.

## Quick Start

1. Add `"redactor"` to your `INSTALLED_APPS` setting as follows:

```python
INSTALLED_APPS = [
    ...
    'redactor',
]
```

2. Include the Redactor URL configuration in your project's `urls.py`:

```python
path('', include('redactor.urls')),
```

3. Run `python manage.py migrate` to create the Redactor models.

4. Copy your Redactor library files into the `static` folder in your project:

```
vendor/redactor/redactor.min.css
vendor/redactor/redactor.min.js
vendor/redactor/plugins/imagemanager.min.js
vendor/redactor/plugins/video.min.js
vendor/redactor/plugins/widget.min.js
```

5. Add Redactor support to your model in `admin.py`:

```python
from django.contrib import admin
from redactor.mixins import RedactorMixin
from .models import Post

@admin.register(Post)
class PostAdmin(RedactorMixin, admin.ModelAdmin):
    ...
    redactor_fields = ['content']
    ...
```

`content` is a `TextField` attribute in the `Post` model.
You can specify multiple fields if needed.

## Releasing a New Version

Make sure you have an API token for PyPI: https://pypi.org/help/#apitoken

Increase the version number at `pyproject.toml` and create a Git tag:

```bash
rm -rf dist/
uv run python -m build
uv run python -m twine upload dist/*
```

Built at [axiacore](https://axiacore.com).
