from django.urls import path

from .views import RedactorView

app_name = 'redactor'

urlpatterns = [
    path('redactor/file/', RedactorView.as_view(), name='redactor_file')
]
