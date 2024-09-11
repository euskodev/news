from django.contrib import admin
from django.urls import path,include
from applications import home
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')),
    path('tynymce/', include('tinymce.urls')),
]







