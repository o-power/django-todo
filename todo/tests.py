from django.test import TestCase

# Create your tests here.
class TestDjango(TestCase):

    # methods must start with test_
    # a method not starting with test_ is just a supporting method
    def test_is_this_thing_on(self):
        self.assertEqual(1, 1)
