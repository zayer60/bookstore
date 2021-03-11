from django.urls import path
from .views import *

urlpatterns =[
    path('',OrderProcess.as_view(), name='order-process'),
]