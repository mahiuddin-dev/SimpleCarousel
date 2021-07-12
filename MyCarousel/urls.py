from django.urls import path

from . import views


app_name = 'MyCarousel'

urlpatterns = [
    path('', views.Home, name='MyCarousel' ),
]
