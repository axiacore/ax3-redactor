import os, uuid
from django.utils.text import slugify
from django.db import models


def get_upload_path(instance, filename):
    """Returns a unique path up to 100 characters.
    """
    name, ext = os.path.splitext(filename)
    path = os.path.join(
        instance._meta.object_name.lower(),
        uuid.uuid4().hex,
        slugify(name),
    )
    return f'{path[:90]}{ext[:10]}'


class RedactorFile(models.Model):
    file = models.FileField(
        upload_to=get_upload_path,
    )

    name = models.CharField(max_length=255)

    is_image = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
