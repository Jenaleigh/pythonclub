from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getMeeting/', views.getMeeting, name='meeting'),
]

from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
]