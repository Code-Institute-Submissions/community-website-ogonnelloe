from unittest import TestCase
from django.test import Client
from .forms import CommentForm
from .views import CommunityUpdatesMostRecent

class TestCommentForm(TestCase):

    def test_empty_comment(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())

    def test_comment(self):
        form = CommentForm({'body': 'hello I\'m a comment!'})
        self.assertTrue(form.is_valid())


class TestIndexMostRecent(TestCase):

    def setUp(self):
        self.client = Client()

    def test_most_recent(self):
        response = self.client.get('')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Ogonnelloe', str(response.content))
        self.assertIn('recent_posts', response.context)

# TODO: class TestDetailedView()

class TestCommunityUpdateLike(TestCase):

    def setUp(self):
        self.client = Client()

    def test_like(self):
        response = self.client.post('like/2')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)