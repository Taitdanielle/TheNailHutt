from django.test import TestCase
from .models import Event


class TestEventsModels(TestCase):

    def test_event_created_correctly(self):

        event1 = Event.objects.create(weekday = 'Monday',time = "10:00", description = "Mega Mondays - mega savings")
        event2 = Event.objects.create(weekday = 'Saturday', time = "20:00", description = "Star Saturdays - sing a long")
        event1.save()
        event2.save()
        self.assertEquals(event1.weekday, 'Monday')
        self.assertEquals(event1.time, '10:00')
        self.assertEquals(event1.description, 'Mega Mondays - mega savings')
        self.assertEquals(event2.weekday, 'Saturday')
        self.assertEquals(event2.time, '20:00')
        self.assertEquals(event2.description, 'Star Saturdays - sing a long')


    
    def test__str_method_returns_weekday(self):

        event = Event.objects.create(weekday = 'Monday',time = "10:00", description = "Mega Mondays - mega savings")

        self.assertEqual(event.__str__(), "Monday")
    