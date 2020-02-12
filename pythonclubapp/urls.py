from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getMeeting/', views.getMeeting, name='meetings'),
    path('getResourceType/', views.getResourceType, name='resourcetypes'),
    path('getResource/', views.getResource, name='resources'),
    path('loginMessage/', views.loginMessage, name='loginmessage'),
    path('logoutMessage/', views.logoutMessage, name='logoutmessage'),
    path('resourcedetails/<int:id>', views.resourceDetails, name='resourcedetails'),
]