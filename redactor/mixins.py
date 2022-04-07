class RedactorMixin:
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        for field in getattr(self, 'redactor_fields', []):
            form.base_fields[field].widget.attrs['enable-redactor'] = True

        for field in getattr(self, 'basic_redactor_fields', []):
            form.base_fields[field].widget.attrs['enable-basic-redactor'] = True

        return form

    class Media:
        css = {
            'all': (
                'vendor/redactor/redactor.min.css',
                'redactor/admin-redactor.css',
            )
        }
        js = (
            'vendor/redactor/redactor.min.js',
            'vendor/redactor/plugins/imagemanager.min.js',
            'vendor/redactor/plugins/video.min.js',
            'vendor/redactor/plugins/widget.min.js',
            'redactor/admin-redactor.js',
        )
