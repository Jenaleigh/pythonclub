from django.contrib import admin
from .models import Meeting, ResourceType, Resource, MeetingMinutes, Event

# Register your models here.

admin.site.register(Meeting)
admin.site.register(ResourceType)
admin.site.register(Resource)
admin.site.register(MeetingMinutes)
admin.site.register(Event)
