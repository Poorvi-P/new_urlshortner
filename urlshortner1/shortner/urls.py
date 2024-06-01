from django.urls import path
from shortner.views import *
urlpatterns = [
    path('hello', hello, name='hello'),
    path('create', create, name='create'),
    path('<str:pk>', go, name='go')
]
