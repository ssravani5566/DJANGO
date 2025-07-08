from django.urls import path
from . import views

urlpatterns = [
    path('', views.yellow_home, name='yellow_home'),
]
