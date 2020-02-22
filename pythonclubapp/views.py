from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, ResourceType, Event
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
def index (request):
    return render(request, 'pythonclubapp/index.html')

def getMeeting(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'pythonclubapp/meeting.html',{'meetings_list': meetings_list})

def getMeetingMinutes(request):
    meetingminutes_list=MeetingMinutes.objects.all()
    return render(request, 'pythonclubapp/meetingminutes.html',{'meetingminutes_list': meetingminutes_list})

@login_required
def getResourceType(request):
    resourcetype_list=ResourceType.objects.all()
    return render(request, 'pythonclubapp/resourcetype.html', {'resourcetype_list': resourcetype_list})

def getResource(request):
    resource_list=Resource.objects.all()
    return render(request, 'pythonclubapp/resource.html', {'resource_list': resource_list})

def resourceDetails(request, id):
    resource=get_object_or_404(Resource, pk=id)
    context={
        'resource': resource,
    }
    return render(request, 'pythonclubapp/resourcedetails.html', context=context)

def loginMessage(request):
    return render(request, 'pythonclubapp/loginmessage.html')

def logoutMessage(request):
    return render(request, 'pythonclubapp/logoutmessage.html')

