from django.urls import path

from . import views

app_name = 'djadesh'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ItemView.as_view(), name='detail'),
    path('<int:item_id>/add/', views.BasketCount.as_view(), name='add'),
    path('basket/', views.Basket.as_view(), name='basket'),
]
