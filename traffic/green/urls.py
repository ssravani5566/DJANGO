from django.urls import path
from . import views

urlpatterns = [
    path('', views.green_home, name='green_home'),
]
