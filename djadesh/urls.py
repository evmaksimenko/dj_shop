from django.urls import path

from . import views

app_name = 'djadesh'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
]
