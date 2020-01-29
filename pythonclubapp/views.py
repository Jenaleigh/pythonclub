from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, ResourceType, Event

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'pythonclubapp/index.html')

def getMeeting(request):
    type_list=Meeting.objects.all()
    return render(request, 'pythonclubapp/meeting.html',{'type_list': type_list})

def getResourceType(request):
    type_list=ResourceType.objects.all()
    return render(request, 'pythonclubapp/resourcetype.html', {'type_list': type_list})

def getResource(request):
    type_list=Resource.objects.all()
    return render(request, 'pythonclubapp/resource.html', {'type_list': type_list})

