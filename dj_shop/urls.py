from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.utils.functional import curry
from django.views.defaults import *

urlpatterns = [
    path('shop/', include('djadesh.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = curry(server_error, template_name='500.html')
handler404 = curry(page_not_found, template_name='404.html')
