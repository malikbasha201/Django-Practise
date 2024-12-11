from django.urls import path
from ssmb.views import *

urlpatterns = [
    path('superstar/',superstar,name='superstar'),
]
