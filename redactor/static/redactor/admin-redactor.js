(function ($) {
    $(document).ready(function () {
        $R('textarea[enable-redactor]', {
            linkTarget: '_blank',
            plugins: ['imagemanager', 'video', 'widget'],
            fileUpload: '/redactor/file/',
            imageUpload: '/redactor/file/',
            imageManagerJson: '/redactor/file/',
            imageResizable: true,
            imagePosition: true
        });

        $R('textarea[enable-basic-redactor]', {
            linkTarget: '_blank',
            buttons: ['bold', 'italic', 'underline'],
        });
    });
})(django.jQuery);
