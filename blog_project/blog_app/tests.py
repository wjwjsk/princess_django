from django.test import TestCase
from .models import Topic

class MyModelTestCase(TestCase):
    def testMethod(self):
        topic_id = '0'
        try:
            topic = Topic.objects.all()
            print(topic)
            return topic
        except Topic.DoesNotExist:
            return None
        self.assertEqual(1, 1)


