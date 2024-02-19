from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post
# Create your tests here.

class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixtures.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "post 1"
        p1_tester = Post(title=expected)
        actual = str(p1_tester)
        self.assertEqual(expected, actual)
