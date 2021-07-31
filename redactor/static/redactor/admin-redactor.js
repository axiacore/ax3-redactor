django.jQuery(() => {
    $R('textarea[enable-redactor]', {
        linkTarget: '_blank',
        plugins: ['imagemanager', 'video', 'widget'],
        fileUpload: '/redactor/file/',
        imageUpload: '/redactor/file/',
        imageManagerJson: '/redactor/file/',
        imageResizable: true,
        imagePosition: true
    });
});
