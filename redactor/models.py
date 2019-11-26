from django.db import models

from ax3_model_extras.storages import get_upload_path


class RedactorFile(models.Model):
    file = models.FileField(upload_to=get_upload_path)

    name = models.CharField(max_length=255)

    is_image = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
