from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('add', views.add, name='add'),
    path('Image', views.image, name='Image'),
]