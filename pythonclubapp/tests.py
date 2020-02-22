from django.test import TestCase
from .models import ResourceType, Resource, Meeting, MeetingMinutes, Event

class ResourceTypeTest(TestCase):
    def test_string(self):
        type=ResourceType(typename="Website")
        self.assertEqual(str(type), type.typename)

    def test_table(self):
        self.assertEqual(str(ResourceType._meta.db_table), 'resourcetypes')

class ResourceTest(TestCase):
    def setup(self):
        type=ResourceType(typename="Website")
        resource=Resource(resource='Py4e', resourcetype=type)
        return resource
    
    def test_string(self):
        res=self.setup()
        self.assertEqual(str(res), res.resource)
    
    def test_type(self):
        res=self.setup()
        self.assertEqual(str(Resource._meta.db_table), 'website')

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resources')

class MeetingTest(TestCase):
    def test_string(self):
        meet=Meeting(meeting="Meeting 1")
        self.assertEqual(str(meet), meet.meeting)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meetings')

class MeetingMinutesTest(TestCase):
    def test_string(self):
        mm=MeetingMinutes(mmname="Meeting 1 Minutes")
        self.assertEqual(str(mm), mm.mmname)

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class EventTest(TestCase):
    def test_string(self):
        event=Event(eventname="Python Club Mixer")
        self.assertEqual(str(event), event.eventname)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'events')