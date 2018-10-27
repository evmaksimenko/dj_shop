from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'djadesh'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ItemView.as_view(), name='detail'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
