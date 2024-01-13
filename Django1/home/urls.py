from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contactus', contact, name='contactus'),
    path('my_services', service, name='my_services'),
    path('my_portfolio', portfolio, name='my_portfolio'),
    path('pricing', price, name='pricing'),
    path('aboutus', about, name='aboutus'),
]