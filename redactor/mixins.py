class RedactorMixin:
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        for field in self.redactor_fields:
            form.base_fields[field].widget.attrs['enable-redactor'] = True
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
