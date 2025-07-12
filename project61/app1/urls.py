from django.urls import path
from . import views
urlpatterns = [
   path('',views.home, name='home'),
   path('101/',views.page_101,name='page_101'),
   path('102/',views.page_102,name='page_102'),
   path('103/',views.page_103,name='page_103'),
   path('104/',views.page_104,name='page_104'),
   path('105/',views.page_105,name='page_105'),
   path('106/',views.page_106,name='page_106'),
   path('107/',views.page_107,name='page_107'),
   path('108/',views.page_108,name='page_108'),
  
   
	]