from django.test import TestCase
from .models import Profile

class ProfileTestClass(TestCase):
  """
  model tests to test profile class functionality
  """
  def setUp(self):
    self.james= Profile(user = "john", image ='profile.jpg')
  def test_instance(self):
        self.assertTrue(isinstance(self.james,Profile))
