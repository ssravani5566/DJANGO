from django.urls import path
from . import views

urlpatterns = [
    path('', views.red_home, name='red_home'),
]
