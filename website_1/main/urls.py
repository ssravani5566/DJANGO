from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('aliya/', views.aliya, name='aliya'),
    path('sravani/', views.sravani, name='sravani'),
    path('pavani/', views.pavani, name='pavani'),
    path('varsha/', views.varsha, name='varsha'),
    path('pinky/', views.pinky, name='pinky'),
]
