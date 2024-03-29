from ax3_model_extras.storages import get_storage, get_upload_path
from django.db import models


class RedactorFile(models.Model):
    file = models.FileField(
        upload_to=get_upload_path,
        storage=get_storage(),
    )

    name = models.CharField(max_length=255)

    is_image = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
