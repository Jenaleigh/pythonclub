from django.urls import path, include

urlpatterns = [
]

from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
]