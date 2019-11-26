django.jQuery(() => {
    $R('textarea[enable-redactor]', {
        linkTarget: '_blank',
        plugins: ['imagemanager', 'video'],
        fileUpload: '/redactor/file/',
        imageUpload: '/redactor/file/',
        imageManagerJson: '/redactor/file/'
    });
});
