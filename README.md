# AX3 Redactor

This app is part of the AX3 technology developed by Axiacore.

It will allow to use redactor inside the django admin interface.

## Quick start

1. Add "redactor" to your INSTALLED_APPS setting like this:

```python
    INSTALLED_APPS = [
        ...
        'redactor',
    ]
```

2. Include the redactor URLconf in your project urls.py like this:

```python
    path('', include('redactor.urls')),
```

3. Run `python manage.py migrate` to create the redactor models.

4. Copy this redactor library files into a `static` folder in your proyect:

```python
    vendor/redactor/redactor.min.css
    vendor/redactor/redactor.min.js
    vendor/redactor/plugins/imagemanager.min.js
    vendor/redactor/plugins/video.min.js
    vendor/redactor/plugins/widget.min.js
```

5. Add to the admin.py the redactor support for a given model:

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

`content` is a `TextField` attribute at the `Post` model.
You can use multiple fields.

## Releasing a new version

Make sure you have an API Token for PyPI: https://pypi.org/help/#apitoken

Make sure you increase the version number and create a git tag:

```bash
$ python3 -m pip install --user --upgrade setuptools wheel twine
$ ./release.sh
```

Made by [Axiacore](https://axiacore.com).
