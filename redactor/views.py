from io import BytesIO

from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from ax3_model_extras.webp import generate_webp

from PIL import Image, UnidentifiedImageError

from .models import RedactorFile


@method_decorator(csrf_exempt, name='dispatch')
class RedactorView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

    def get(self, request, *args, **kwargs):
        return JsonResponse([
            {
                'thumb': obj.file.url, 'url': obj.file.url, 'id': obj.id, 'title': obj.name
            } for obj in RedactorFile.objects.filter(is_image=True)[:20]
        ], safe=False)

    def post(self, request, *args, **kwargs):
        count = 0
        images = {}
        for file in request.FILES.getlist('file[]'):
            try:
                output_image = Image.open(file)
                img_format = output_image.format
                if output_image.format == 'JPEG':
                    output_image = output_image.convert('RGB')

                bytes_io = BytesIO()
                output_image.save(bytes_io, format=img_format, optimize=True)

                obj = RedactorFile.objects.create(
                    file=SimpleUploadedFile(file.name, bytes_io.getvalue()),
                    name=file.name,
                    is_image=True,
                )
                generate_webp(image_field=obj.file)
            except UnidentifiedImageError:
                obj = RedactorFile.objects.create(file=file, name=file.name, is_image=False)

            images['file-{}'.format(count)] = {'url': obj.file.url, 'name': obj.name, 'id': obj.id}
            count += 1

        return JsonResponse(images, safe=False)
