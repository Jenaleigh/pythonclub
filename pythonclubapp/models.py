from django.db import models
from django.contrib.auth.models import User

class ResourceType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255, null=True, blank=True)

    def _str_(self):
        return self.typename
    
    class Meta:
        db_table='resourcetype'
        verbose_name_plural='resourcetypes'

class Resource(models.Model):
    rName=models.CharField(max_length=255)
    rType=models.ForeignKey(ResourceType, on_delete=models.DO_NOTHING)
    rURL=models.URLField(null=True, blank=True)
    dateEntered=models.DateField()
    userID=models.ForeignKey(User, on_delete=models.CASCADE)
    rDescription=models.TextField()

    def _str_(self):
        return self.rName
    
    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Meeting(models.Model):
    meetingTitle=models.CharField(max_length=255)
    meetingDate=models.DateField()
    meetingTime=models.CharField(max_length=255)
    meetingLocation=models.CharField(max_length=255)
    meetingAgenda=models.TextField()

    def _str_(self):
        return self.meetingTitle

    class Meta:
        db_table='meetinginformation'

class MeetingMinutes(models.Model):
    meetingID=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance=models.ManyToManyField(User)
    minutes=models.TextField()
    meetingminutesURL=models.URLField(null=True, blank=True)

    def _str_(self):
        return self.meetingID

    class Meta:
        db_table='minutes'

class Event(models.Model):
    eTitle=models.CharField(max_length=255)
    eLocation=models.CharField(max_length=255)
    eDate=models.DateField()
    eTime=models.TimeField()
    eDescription=models.TextField
    eHostUserID=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    eURL=models.URLField(null=True, blank=True)
  

    def _str_(self):
        return self.eTitle
    
    class Meta:
        db_table='event'
        verbose_name_plural='events'



